# Резаева Оля
from typing import Type, Optional
from crewai.tools import BaseTool
from pydantic import BaseModel, Field, PrivateAttr
from openai import OpenAI
import os

# Схема входных параметров
class MermaidDiagramInput(BaseModel):
    diagram_type: str = Field(
        description="Тип диаграммы: flowchart, sequence, class, er, pie, gantt, state, user-journey"
    )
    description: str = Field(
        description="Описание того, что должна отображать диаграмма"
    )
    style: Optional[str] = Field(
        default="professional",
        description="Стиль диаграммы: professional, simple, detailed"
    )

class GenerateMermaidDiagramTool(BaseTool):
    name: str = "generate_mermaid_diagram"
    description: str = (
        "Генерирует код диаграммы в формате Mermaid.js на основе текстового описания. "
        "Полезно для визуализации архитектуры, процессов, последовательностей и связей между данными. "
        "Поддерживаемые типы: flowchart (блок-схема), sequence (диаграмма последовательности), "
        "class (диаграмма классов), er (ER-диаграмма), pie (круговая диаграмма), "
        "gantt (диаграмма Ганта), state (диаграмма состояний), user-journey (путь пользователя)."
    )
    args_schema: Type[BaseModel] = MermaidDiagramInput
    
    # Объявляем client как приватный атрибут, который Pydantic не будет проверять
    _client: Optional[OpenAI] = PrivateAttr(default=None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        api_key = os.getenv("DEEPSEEK_API_KEY")
        if not api_key:
            raise ValueError("DEEPSEEK_API_KEY не найден в переменных окружения")

        # Используем _client вместо client
        self._client = OpenAI(
            api_key=api_key,
            base_url="https://api.deepseek.com/v1"
        )

    def _run(self, diagram_type: str, description: str, style: str = "professional") -> str:
        """Генерирует Mermaid-диаграмму через DeepSeek API"""

        prompt = f"""Ты - эксперт по созданию диаграмм в формате Mermaid.js.

Твоя задача: создать {diagram_type} диаграмму на основе описания ниже.

Требования:
1. Код должен быть валидным Mermaid.js синтаксисом
2. Используй понятные названия узлов и связей
3. Добавь комментарии на русском языке (после %%)
4. Стиль: {style}
5. Верни ТОЛЬКО Mermaid код, без пояснений и Markdown

Описание:
{description}

Примеры для разных типов:

FLOWCHART:
flowchart TD
    A[Начало] --> B{{Принятие решения}}
    B -->|Да| C[Действие 1]
    B -->|Нет| D[Действие 2]
    C --> E[Конец]
    D --> E

SEQUENCE:
sequenceDiagram
    participant Пользователь
    participant Сервер
    participant БазаДанных
    Пользователь->>Сервер: Запрос данных
    Сервер->>БазаДанных: SQL запрос
    БазаДанных-->>Сервер: Результат
    Сервер-->>Пользователь: Ответ

Теперь создай {diagram_type} диаграмму.
Верни только код Mermaid, без обрамления в тройные кавычки.
"""

        try:
            response = self._client.chat.completions.create(  # используем _client
                model="deepseek-chat",
                messages=[
                    {"role": "system", "content": "Ты эксперт по Mermaid.js. Отвечай только кодом диаграммы без лишних слов."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )

            mermaid_code = response.choices[0].message.content.strip()
            mermaid_code = mermaid_code.replace("```mermaid", "").replace("```", "").strip()

            return f"```mermaid\n{mermaid_code}\n```"

        except Exception as e:
            return self._get_fallback_diagram(diagram_type, description)

    def _get_fallback_diagram(self, diagram_type: str, description: str) -> str:
        """Возвращает диаграмму-заглушку при ошибке API"""

        templates = {
            "flowchart": "```mermaid\nflowchart TD\n    A[Начало анализа: {desc}] --> B{{Проверка условий}}\n    B -->|Условие выполнено| C[Выполнить действие]\n    B -->|Условие не выполнено| D[Альтернативный путь]\n    C --> E[Завершение]\n    D --> E\n```",
            "sequence": "```mermaid\nsequenceDiagram\n    participant Клиент\n    participant Сервер\n    participant БД\n\n    Клиент->>Сервер: Отправить запрос\n    activate Сервер\n    Сервер->>БД: Выполнить операцию\n    activate БД\n    БД-->>Сервер: Вернуть результат\n    deactivate БД\n    Сервер-->>Клиент: Ответить клиенту\n    deactivate Сервер\n```",
            "class": "```mermaid\nclassDiagram\n    class MainClass {{\n        +string name\n        +void process()\n        -bool _validate()\n    }}\n    class SubClass {{\n        +void execute()\n    }}\n    MainClass <|-- SubClass\n```",
            "er": "```mermaid\nerDiagram\n    ENTITY1 {{\n        int id PK\n        string name\n    }}\n    ENTITY2 {{\n        int id PK\n        int entity1_id FK\n    }}\n    ENTITY1 ||--o{{ ENTITY2 : has\n```"
        }

        template = templates.get(diagram_type, templates["flowchart"])
        return template.format(desc=description[:50])

    async def _arun(self, diagram_type: str, description: str, style: str = "professional") -> str:
        """Асинхронная версия (опционально)"""
        return self._run(diagram_type, description, style)