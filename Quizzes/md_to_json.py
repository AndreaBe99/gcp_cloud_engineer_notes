import re
import json
from typing import Dict, List

# Modify the path to the markdown file containing the questions and answers
LINUX_PATH = "/home/andrea/Documenti"
WINDOWS_PATH = "C:/Users/an.bernini/WORKAREA/Certificazione GCP"
ANDROID_PATH = "/storage/emulated/0/Documents"
# Choose platform
ABS_PATH = [LINUX_PATH, WINDOWS_PATH, ANDROID_PATH][1]

PATH = f"{ABS_PATH}/gcp_cloud_engineer_notes/Quizzes/exam_topics.md"


def markdown_to_json(markdown_text: str) -> Dict[str, Dict[str, str]]:
    """
    Converts a markdown string into a dictionary format suitable for JSON conversion.

    Args:
        markdown_text (str): The content of the markdown file containing questions and answers.

    Returns:
        Dict[str, Dict[str, str]]: A dictionary where each key is the question number,
        and the value is another dictionary containing the question, choices, and answers.
    """
    exam_data: Dict[str, Dict[str, str]] = {}

    # Split the markdown content into sections based on "#### Question"
    sections = markdown_text.split('#### Question')
    
    for section in sections[1:]:
        # Extract the question number
        question_number = re.search(r'(\d+)', section).group(1)
        
        # Extract the question text
        question_text = re.search(r'\d+\n\n(.+?)\n\n', section, re.DOTALL).group(1).strip()
        # Delete "\n" from the question text
        question_text = question_text.replace("\n", " ")
        
        # Extract the multiple-choice options
        choices_matches = re.findall(r'\n([A-E])\.\s(.+)', section)
        choices = {choice[0]: choice[1].strip() for choice in choices_matches}
        
        # Extract the correct answers, ignoring parentheses
        answer_text = re.search(r'\*\*Answer:\s(.+)\*\*', section).group(1).strip()
        
        # Handle multiple answers in the format "A-B" or single answers like "D"
        answer = re.split(r'[-\s]', answer_text.split('(')[0].strip())  # Ignore parentheses, split multiple answers
        answer = [x for x in answer if x]  # Remove any empty strings

        # Add the question data to the dictionary
        exam_data[question_number] = {
            "question": question_text,
            "choices": choices,
            "answers": answer
        }
    
    return exam_data


def read_markdown_file(path: str) -> str:
    """
    Reads the content of a markdown file.

    Args:
        path (str): The file path to the markdown file.

    Returns:
        str: The content of the markdown file as a string.
    """
    with open(path, 'r', encoding='utf-8') as file:
        return file.read()


def save_json_file(data: Dict[str, Dict[str, str]], path: str) -> None:
    """
    Saves a dictionary as a formatted JSON file.

    Args:
        data (Dict[str, Dict[str, str]]): The dictionary containing the questions and answers.
        path (str): The file path where the JSON will be saved.
    """
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

if __name__ == '__main__':
    # Read the markdown file
    markdown_content = read_markdown_file(PATH)

    # Convert the markdown to a JSON-like dictionary
    exam_json = markdown_to_json(markdown_content)

    # Save the dictionary to a JSON file
    save_json_file(exam_json, PATH.replace('.md', '.json'))

    # Print the JSON data to the console (formatted)
    print(json.dumps(exam_json, indent=4, ensure_ascii=False))
