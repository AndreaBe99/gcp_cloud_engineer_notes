import random
import re

from enum import Enum
from typing import List, Tuple


# Modify the path to the markdown file containing the questions and answers
LINUX_PATH = "/home/andrea/Documenti"
WINDOWS_PATH = "C:/Users/an.bernini/WORKAREA"
ANDROID_PATH = "/storage/emulated/0/Documents"
# Choose platform
ABS_PATH = [LINUX_PATH, WINDOWS_PATH, ANDROID_PATH][0]

PATH = f"{ABS_PATH}/gcp_cloud_engineer_notes/Quizzes/exam_topics.md"


class Color(Enum):
    """ANSI color codes for terminal output."""

    PURPLE = "\033[95m"
    CYAN = "\033[96m"
    DARKCYAN = "\033[36m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RED = "\033[91m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    END = "\033[0m"


def extract_questions(num_questions=50) -> List[Tuple[str, str]]:
    """
    Extract the questions and answers from a markdown file.

    Args:
        num_questions (int): The number of questions to extract.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the questions and answers.
    """
    # Read the content of the markdown file
    with open(PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract the questions and answers from the content
    questions = re.findall(
        r"#### Question \d+\n\n(.*?)\n\n\*\*Answer: (.*?)\*\*", content, re.DOTALL
    )

    # Select a random sample of questions
    selected_questions = random.sample(questions, min(num_questions, len(questions)))

    return selected_questions


def simulate_exam() -> None:
    """Simulate an exam in the terminal."""
    # Extract the questions and answers
    selected_questions = extract_questions()

    correct_answers = 0
    # Show each question and ask the user for an answer
    for i, (question, answer) in enumerate(selected_questions, 1):

        # Split the question and the choices
        quest, choices = question.split("\n\n")
        print(f"{Color.BOLD.value}Question {i}:\n{quest}{Color.END.value}", end="\n\n")
        print(choices, end="\n\n")

        user_answer = input("Your answer: ").strip().upper()

        # Get only the most voted answer
        answer = answer.split(" ")[0].upper()

        # Check if the answer is correct and provide feedback
        if user_answer in answer:
            print(f"{Color.GREEN.value}Correct!{Color.END.value}", end="\n\n")
            correct_answers += 1
        else:
            print(
                f"{Color.RED.value}Wrong!{Color.END.value} The correct answer was: {answer}",
                end="\n\n",
            )
        print("-" * 50)

    # Calculate and print the final score
    print(f"Your score: {correct_answers}/{len(selected_questions)}")


if __name__ == "__main__":
    simulate_exam()
