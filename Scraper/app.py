import json
import os
import traceback
from typing import Any

from src.exam_scraper import ExamScraper
from src.parser import prepare_parser


def save_json_file(data: dict) -> None:
    """
    Save the question and answer data to a JSON file.

    Args:
        data (dict): Data to save to the JSON file
    """
    # Check if the JSON file already exists, and load its content if so
    file_name = "quiz_scraping.json"
    if os.path.exists(file_name):
        with open(file_name, "r", encoding="utf-8") as file:
            existing_data = json.load(file)
    else:
        existing_data = {}

    # Update existing data with the new question
    existing_data.update(data)

    # Write the updated data back to the JSON file
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(
            existing_data,
            file,
            ensure_ascii=False,
            indent=4,
        )


def q_and_a_scraping(exam_id: str, start: int, end: int) -> None:
    """
    Fetch the question and answer from the page and save it to a JSON file.

    Args:
        exam_id (str): The exam ID of Exam Topic
        start (int): The starting question index
        end (int): The ending question index
    """
    print(f"Scraping questions {start} to {end} for {exam_id} exam")
    scraper = ExamScraper(exam_id)
    for question_index in range(start, end + 1):
        try:
            soup = scraper.get_page(question_index)
            question_text, choices = ExamScraper.get_question_text(soup)
            answer_text = ExamScraper.get_answer_text(soup)
            most_voted_answer = ExamScraper.get_most_voted_answer_text(soup)

            data = {
                str(question_index): {
                    "question": question_text.split("\n")[0].strip(),
                    "choices": choices,
                    "answers": [answer_text],
                    "most_voted_answer": most_voted_answer,
                }
            }
            save_json_file(data)

        except Exception as e:
            print(f"Error saving question {question_index}: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    options = prepare_parser().parse_args()
    q_and_a_scraping(
        options.exam,
        options.start,
        options.end,
    )
