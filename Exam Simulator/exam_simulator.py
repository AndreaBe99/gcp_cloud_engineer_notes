import random
import re

from typing import List, Tuple


def extract_questions(
    file_path: str = "Quizzes/exam_topics.md",
    num_questions=50,
) -> List[Tuple[str, str]]:
    """
    Extract the questions and answers from a markdown file.

    Args:
        file_path (str): The path to the markdown file containing the questions and answers.
        num_questions (int): The number of questions to extract.

    Returns:
        List[Tuple[str, str]]: A list of tuples containing the questions and answers.
    """
    # Read the content of the markdown file
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Extract the questions and answers from the content
    questions = re.findall(
        r"#### Question \d+\n\n(.*?)\n\n\*\*Answer: (.*?)\*\*", content, re.DOTALL
    )

    # Select a random sample of questions
    selected_questions = random.sample(questions, min(num_questions, len(questions)))

    return selected_questions


def simulate_exam() -> None:
    """
    Simulate an exam in the terminal.

    Args:
        file_path (str): The path to the markdown file containing the questions and answers.
        num_questions (int): The number of questions to present to the user.
    """
    # Extract the questions and answers
    selected_questions = extract_questions()
    
    correct_answers = 0
    # Show each question and ask the user for an answer
    for i, (question, answer) in enumerate(selected_questions, 1):
        print(f"Question {i}:\n{question}\n")
        user_answer = input("Your answer: ").strip().upper()
        
        # Check if the answer is correct and provide feedback
        if user_answer in answer:
            print("Correct!\n")
            correct_answers += 1
        else:
            print(f"Wrong! The correct answer was: {answer}\n")

    # Calculate and print the final score
    print(f"Your score: {correct_answers}/{len(selected_questions)}")


if __name__ == "__main__":
    simulate_exam()
