import random
import re

from enum import Enum
from typing import List, Tuple


# Modify the path to the markdown file containing the questions and answers
LINUX_PATH = "/home/andrea/Documenti"
WINDOWS_PATH = "C:/Users/an.bernini/WORKAREA/Certificazione GCP"
ANDROID_PATH = "/storage/emulated/0/Documents"
# Choose platform
ABS_PATH = [LINUX_PATH, WINDOWS_PATH, ANDROID_PATH][1]

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


def extract_questions(num_questions=50) -> List[Tuple[str, str, str, str, str, str]]:
    """
    Extract the questions and answers from a markdown file.

    Args:
        num_questions (int): The number of questions to extract.

    Returns:
        List[Tuple[str, str, str, str, str, str]]: A list of tuples containing the
            index, question, the four choices, and the correct answer.
    """
    # Read the content of the markdown file
    with open(PATH, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract the questions and answers using a regular expression
    pattern = r"#### Question (\d+)(.*?)\n\n(A\..*?)(B\..*?)(C\..*?)(D\..*?)\n\n\*\*Answer: (.*?)\*\*"
    matches = re.findall(pattern, content, re.DOTALL)

    # Select a random sample of questions
    selected_questions = random.sample(matches, min(num_questions, len(matches)))

    return selected_questions


def simulate_exam() -> None:
    """Simulate an exam in the terminal."""
    # Extract the questions and answers
    selected_questions = extract_questions()

    # Print the instructions
    print(
        f"{Color.BOLD.value}Welcome to the Exam Simulator!{Color.END.value}\n"
        "You will be presented with a series of multiple-choice questions.\n"
        "Please select the letter(s) corresponding to the correct answer(s).\n"
        f"{Color.YELLOW.value}If the question has multiple correct answers, you need to write the letters separated by a '-'.{Color.END.value}\n"
        "Let's get started!\n"
    )

    correct_answers = 0
    # Show each question and ask the user for an answer
    for i, question in enumerate(selected_questions, 1):
        index, text, *choices, answer = question
        # Delete " \n\n" at the start of the question
        text = text.replace("\n\n", "")
        # Get only the most voted answer
        answer = answer.split(" ")[0].upper()
        
        # Replace newlines in the choices
        choices = [choice.replace("\n", " ") for choice in choices]
        # Split the choices into the letter and the text
        try:
            choices_A, choices_B, choices_C, choices_D, choices_E = choices
        except ValueError:
            choices_A, choices_B, choices_C, choices_D = choices    
            choices_E = None

        # Print the question
        print(f"{Color.BOLD.value}Question {i} (n° {index}):{Color.END.value}")
        print(f"{Color.BOLD.value}{text}{Color.END.value}", end="\n\n")
        
        # Print the choices
        print(f"{Color.GREEN.value}{choices_A[0]}{Color.END.value}{choices_A[1:]}")
        print(f"{Color.RED.value}{choices_B[0]}{Color.END.value}{choices_B[1:]}")
        print(f"{Color.YELLOW.value}{choices_C[0]}{Color.END.value}{choices_C[1:]}")
        if choices_E:
            print(f"{Color.BLUE.value}{choices_D[0]}{Color.END.value}{choices_D[1:]}")
            print(f"{Color.PURPLE.value}{choices_E[0]}{Color.END.value}{choices_E[1:]}", end="\n\n")
        else:
            print(f"{Color.BLUE.value}{choices_D[0]}{Color.END.value}{choices_D[1:]}", end="\n\n")
        
        # Ask the user for an answer
        user_answer = input("Your answer: ").strip().upper()
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
