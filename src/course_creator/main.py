#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from course_creator.crew import CourseCreator

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the crew.
    """
    inputs = {
        'topic': 'Обучение и повторение IT-команды архитектурным решениям и новым трендам'
    }

    try:
        result = CourseCreator().crew().kickoff(inputs=inputs)
        
        # Print the result
        print("\n\n=== FINAL REPORT ===\n\n")
        print(result.raw)

        print("\n\nReport has been saved to output/final_course_ready.md")
        
        print(f"\n--- Статистика использования токенов ---")
        print(f"Всего токенов: {result.token_usage.total_tokens}")
        print(f"Токенов в запросе (prompt): {result.token_usage.prompt_tokens}")
        print(f"Токенов в ответе (completion): {result.token_usage.completion_tokens}")
        print(f"Успешных запросов к LLM: {result.token_usage.successful_requests}")
        print(CourseCreator().crew().usage_metrics)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "topic": "AI LLMs",
        'current_year': str(datetime.now().year)
    }
    try:
        CourseCreator().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CourseCreator().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }

    try:
        CourseCreator().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = CourseCreator().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
