#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from occultismsystem.crew import Occultismsystem

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def format_day (day):
    days = day.split("/")[0]
    month = int(day.split("/")[1])
    year = day.split("/")[2]
    match month:
        case 1:
            smonth = 'January'
        case 2:
            smonth = 'February'
        case 3: 
            smonth = 'March'
        case 4: 
            smonth = 'April'
        case 5: 
            smonth = 'May'
        case 6: 
            smonth = 'June'
        case 7: 
            smonth = 'July'
        case 8: 
            smonth = 'August'
        case 9: 
            smonth = 'September'
        case 10: 
            smonth = 'October'
        case 11: 
            smonth = 'November'
        case 12: 
            smonth = 'December'
        case _:
            smonth = None
    new_day = f'{days} {smonth} {year}'
    return new_day

def run():
    """
    Run the crew.
    """
    language = input("Which your best language? ")
    day = input("Give me your birhtday (example: 1/1/2000): ")
    day = format_day(day)
    hour = input("Then your birth hour (example: 9:30AM): ")
    # Example: 
    # language = "vietnamese"
    # day = "6/7/2006"
    # hour = "12:50PM"
    
    inputs = {
        'topic': f'{hour} {day}',
        'current_year': str(datetime.now().year),
        'target_language': language
    }

    try:
        Occultismsystem().crew().kickoff(inputs=inputs)
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
        Occultismsystem().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Occultismsystem().crew().replay(task_id=sys.argv[1])

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
        Occultismsystem().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

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
        result = Occultismsystem().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")
