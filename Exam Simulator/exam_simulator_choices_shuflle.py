import json
import random
from typing import Dict, List, Tuple
from colorama import Fore, Style, init

# Modify the path to the markdown file containing the questions and answers
LINUX_PATH = "/home/andrea/Documenti"
WINDOWS_PATH = "C:/Users/an.bernini/WORKAREA/Certificazione GCP"
ANDROID_PATH = "/storage/emulated/0/Documents"
# Choose platform
ABS_PATH = [LINUX_PATH, WINDOWS_PATH, ANDROID_PATH][1]

PATH = f"{ABS_PATH}/gcp_cloud_engineer_notes/Quizzes/exam_topics.json"

# Initialize colorama for coloring text in the terminal
init(autoreset=True)

# Define a list of colors to apply only to the choice letters (A, B, C, D)
choice_colors = [
    Fore.YELLOW,
    Fore.RED,
    Fore.GREEN,
    Fore.BLUE,
    Fore.MAGENTA,
]


def load_questions_from_json(path: str) -> Dict[str, Dict[str, str]]:
    """
    Load the questions from the JSON file.

    Args:
        path (str): Path to the JSON file.

    Returns:
        Dict[str, Dict[str, str]]: Dictionary with questions and answers.
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def select_random_questions(
    questions: Dict[str, Dict[str, str]],
    num: int,
) -> List[str]:
    """
    Select a random subset of questions.

    Args:
        questions (Dict[str, Dict[str, str]]): All questions in the dataset.
        num (int): Number of questions to select.

    Returns:
        List[str]: List of randomly selected question numbers.
    """
    return random.sample(list(questions.keys()), num)


def shuffle_choices(
    choices: Dict[str, str],
) -> Tuple[List[Tuple[str, str]], Dict[str, str]]:
    """
    Shuffle the answer choices and reassign letters (A, B, C, etc.).

    Args:
        choices (Dict[str, str]): Dictionary of answer choices.

    Returns:
        Tuple[List[Tuple[str, str]], Dict[str, str]]: A list of shuffled choices with new labels
        and a mapping of old labels to new labels.
    """
    # Extract the original choices as a list of tuples (letter, text)
    original_choices = list(choices.items())

    # Shuffle only the text of the choices
    random.shuffle(original_choices)

    # Reassign letters A, B, C, D, etc. to the shuffled choices
    new_labels = ["A", "B", "C", "D", "E"]
    shuffled_choices = [
        (new_labels[i], original_choices[i][1]) for i in range(len(original_choices))
    ]

    # Create a mapping of old labels to new labels (for updating correct answers)
    old_to_new_label_map = {
        original_choices[i][0]: new_labels[i] for i in range(len(original_choices))
    }

    return shuffled_choices, old_to_new_label_map


def update_correct_answers(
    correct_answers: List[str],
    label_map: Dict[str, str],
) -> List[str]:
    """
    Update the correct answers to reflect the new shuffled choices.

    Args:
        correct_answers (List[str]): The original correct answers.
        label_map (Dict[str, str]): The mapping from old labels to new labels.

    Returns:
        List[str]: The updated correct answers with the new labels.
    """
    return [label_map[answer] for answer in correct_answers]


def ask_question(
    question_data: Dict[str, str],
    original_number: str,
    current_number: int,
):
    """
    Display the question and choices, and get the user's response.

    Args:
        question_data (Dict[str, str]): The question data including text, choices, and answers.
        original_number (str): The original number of the question.
        current_number (int): The current question number in the exam.
    """
    # Display the question number and the original number
    print(
        f"\n{Style.BRIGHT}Question {current_number} (Original #{original_number}){Style.RESET_ALL}"
    )

    # Display the question text in bold
    print(f"{Style.BRIGHT}{question_data['question']}{Style.RESET_ALL}\n")

    # Shuffle and display the choices, along with a mapping to update correct answers
    shuffled_choices, label_map = shuffle_choices(question_data["choices"])

    # Update the correct answers based on the shuffled labels
    correct_answers = update_correct_answers(question_data["answers"], label_map)

    # Display the shuffled choices with colored letters
    for i, (label, text) in enumerate(shuffled_choices):
        color = choice_colors[
            i % len(choice_colors)
        ]  # Cycle through the defined colors
        print(f"{color}{label}{Style.RESET_ALL}. {text}")

    # Get user's answer
    user_answer = input("\nYour answer: ").upper().strip()

    # Check if the answer is correct
    if user_answer in correct_answers:
        print(f"{Fore.GREEN}Correct!{Style.RESET_ALL}\n")
    else:
        correct_text = ", ".join(correct_answers)
        print(
            f"{Fore.RED}Wrong! The correct answer is: {correct_text}{Style.RESET_ALL}\n"
        )
    print("-" * 50)


def run_exam(exam_json: Dict[str, Dict[str, str]], num_questions: int = 50):
    """
    Simulates an exam by selecting random questions and asking the user to answer.

    Args:
        exam_json (Dict[str, Dict[str, str]]): The entire dataset of questions.
        num_questions (int): The number of questions for the exam (default 50).
    """
    # Select random questions
    selected_questions = select_random_questions(exam_json, num_questions)

    print("Welcome to the Exam Simulator!")
    print("You will be presented with a series of multiple-choice questions.")
    print("Please select the letter(s) corresponding to the correct answer(s).")
    print(
        f"{Fore.YELLOW}If the question has multiple correct answers, you need to write the letters separated by a '-'.{Style.RESET_ALL}"
    )

    # Loop over the selected questions and ask one at a time
    for current_number, question_number in enumerate(selected_questions, 1):
        ask_question(exam_json[question_number], question_number, current_number)


# Main code to run the exam simulation
if __name__ == "__main__":
    # Load the questions from the JSON file
    questions = load_questions_from_json(PATH)

    # Run the exam with 50 random questions
    run_exam(questions, num_questions=50)
