# Андреев Дима
import os  # <-- ЭТА СТРОКА ОБЯЗАТЕЛЬНА
from dotenv import load_dotenv
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import (
    SerperDevTool,           # Поиск в интернете через Google
    PDFSearchTool,           # Поиск в PDF-документах
    CSVSearchTool,           # Анализ данных из CSV
    FileReadTool,            # Чтение существующих файлов
    FileWriterTool,
    DirectoryReadTool# ,       # Просмотр структуры папок
    # GitHubSearchTool         
)
from course_creator.tools.mermaid_tool import GenerateMermaidDiagramTool

@CrewBase
class CourseCreator():
    """CourseCreator crew"""

    agents: list[BaseAgent]
    tasks: list[Task]
    
    def __init__(self):
        # Создаём LLM один раз при создании экземпляра класса
        self.deepseek_research_llm = LLM(
            model="deepseek/deepseek-v4-flash",
            base_url="https://api.deepseek.com/v1",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=0.6
        )
        self.deepseek_review_llm = LLM(
            model="deepseek/deepseek-chat",
            base_url="https://api.deepseek.com/v1",
            api_key=os.getenv("DEEPSEEK_API_KEY"),
            temperature=0.3
        )
        
        self.search_tool = SerperDevTool()
        self.file_read = FileReadTool()
        self.file_write = FileWriterTool()
        self.mermaid_tool = GenerateMermaidDiagramTool()
        self.dir_tool = DirectoryReadTool()

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'], # type: ignore[index]
            verbose=True,
            tools=[
                self.search_tool,          # Поиск актуальных источников
                PDFSearchTool(),           # Работа с PDF-документами
                CSVSearchTool(),           # Анализ данных (если есть таблицы)
                self.file_read,            # Чтение существующих материалов
                self.file_write,
                self.dir_tool              # Навигация по файловой системе
            ],
            llm=self.deepseek_research_llm
        )

    @agent
    def analyst_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['analyst_reviewer'], # type: ignore[index]
            verbose=True,
            tools=[
                self.file_read,      # Чтение course_raw.md
                self.file_write,     # Сохранение analyst_review.md
                self.dir_tool        # Проверка структуры output/
            ],
            llm=self.deepseek_review_llm
        )
        
    @agent
    def developer_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config['developer_reviewer'], # type: ignore[index]
            verbose=True,
            tools=[
                self.file_read,      # Чтение course_raw.md
                self.file_write,     # Сохранение analyst_review.md
                self.dir_tool        # Проверка структуры output/
            ],
            llm=self.deepseek_review_llm
        )
        
    @agent
    def illustrator(self) -> Agent:
        return Agent(
            config=self.agents_config['illustrator'], # type: ignore[index]
            verbose=True,
            tools=[
                self.file_read,        # Чтение доработанного курса
                self.file_write,       # Сохранение illustrations.md
                self.search_tool,      # Поиск референсов и идей для иллюстраций
                self.mermaid_tool      # + кастомный инструмент для генерации Mermaid-диаграмм
            ],
            llm=self.deepseek_research_llm
        )

    @task
    def course_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['course_creation_task'], # type: ignore[index]
            output_file='course_raw.md'
        )

    @task
    def analyst_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['analyst_review_task'], # type: ignore[index]
            output_file='analyst_review.md'
        )
        
    @task
    def developer_review_task(self) -> Task:
        return Task(
            config=self.tasks_config['developer_review_task'], # type: ignore[index]
            output_file='developer_review.md'
        )
        
    @task
    def illustration_task(self) -> Task:
        return Task(
            config=self.tasks_config['illustration_task'], # type: ignore[index]
            output_file='illustrations.md'
        )
        
    @task
    def final_assembly_task(self) -> Task:
        return Task(
            config=self.tasks_config['final_assembly_task'], # type: ignore[index]
            output_file='final_course_ready.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CourseCreator crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
            checkpoint=True
        )
