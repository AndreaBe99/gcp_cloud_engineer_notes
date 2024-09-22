from bs4 import BeautifulSoup
import requests

from Scraper.src.parser import prepare_parser
from googlesearch import search
from typing import Union

EXAM = {
    "gcp-ace": {
        "query": "examtopic gcp ace question",
        "keyword": "associate-cloud-engineer-topic-1-question",
    },
}


def get_answer_url(exam_id: str, index: int) -> Union[str, None]:
    """
    Get the URL for the answer page of the question.

    Use the Google search API to find the URL of the answer page for the question.
    For example, the URL for the answer page of question 123 of the GCP ACE exam is:
        examtopic+gcp+ace+question+123

    Args:
        exam_id (str): The ID of the exam
        index (int): The index of the question

    Returns:
        Union[str, None]: The URL of the answer page or None if not found
    """
    query = f"{EXAM[exam_id]['query']} {index}"
    result_urls = list(search(query, sleep_interval=1))

    for url in result_urls:
        if f"{EXAM[exam_id]['keyword']}-{index}" in url:
            print(f"Found URL for question #{index}: {url}")
            return url
    return None


def get_question_text(soup: BeautifulSoup) -> str:
    """
    Get the question text from the page

    Args:
        soup (BeautifulSoup): The parsed HTML page

    Returns:
        str: The question text
    """
    question_body = soup.find("div", class_="question-body")

    # Get question text
    question_text = (
        question_body.find_all(
            "p",
            class_="card-text",
        )[0]
        .get_text()
        .strip()
    )

    # Find the container for the question choices
    question_choices_container = soup.find(
        "div",
        class_="question-choices-container",
    )

    # Extract each choice
    choices = question_choices_container.find_all(
        "li",
        class_="multi-choice-item",
    )

    choices_list = [f"{question_text}\n"]
    # Loop through each choice and print its text
    for choice in choices:
        choice_letter = (
            choice.find(
                "span",
                class_="multi-choice-letter",
            )
            .get_text()
            .strip()
        )
        choice_text = choice.get_text(separator=" ", strip=True)
        choices_list.append(choice_text)

    question_text = "\n".join(choices_list)
    return question_text


def get_answer_text(soup: BeautifulSoup) -> str:
    """
    Get the answer text from the page.

    Example:
    <span class="correct-answer-box"><strong>Suggested Answer:</strong>
        <span class="correct-answer">D</span>
        <a href="#" class="vote-answer-button ml-1 d-print-none" data-toggle="tooltip" title="" data-original-title="Vote an answer">🗳️</a>
        <br>
    </span>

    Args:
        soup (BeautifulSoup): The parsed HTML page

    Returns:
        str: The answer text
    """
    answer_text = soup.find("span", class_="correct-answer").get_text().strip()
    return answer_text


def get_most_voted_answer_text(soup: BeautifulSoup) -> str:
    """
    Get the most voted answer from the page.

    Example:
    <div class="progress vote-distribution-bar">
        <div class="vote-bar progress-bar bg-primary" data-toggle="tooltip" role="progressbar" style="width: 94%; display: flex;" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100" data-original-title="16 votes." title="">B (94%)</div>
        <div class="vote-bar progress-bar bg-info" data-toggle="tooltip" role="progressbar" style="width: 6%; display: flex;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" data-original-title="1 votes." title="">6%</div>
        <div class="vote-bar progress-bar bg-success" data-toggle="tooltip" role="progressbar" style="width: 25%; display: none;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" data-original-title="" title="">B (20%)</div>
        <div class="vote-bar progress-bar bg-warning" data-toggle="tooltip" role="progressbar" style="width: 15%; display: none;" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" data-original-title="" title="">Other</div>
    </div>

    Args:
        soup (BeautifulSoup): The parsed HTML page

    Returns:
        str: The most voted answer text
    """
    # Get the most voted answer
    votes = soup.find("div", class_="progress vote-distribution-bar").find_all(
        "div", class_="vote-bar"
    )
    most_voted_answer = votes[0].get_text().strip()
    return most_voted_answer


def write_markdown_file(
    question_text: str,
    answer_text: str,
    most_voted_answer: str,
    index: int,
) -> None:
    """
    Write the question and answer to a markdown file.

    Args:
        question_text (str): The question text
        answer_text (str): The answer text
        most_voted_answer (str): The most voted answer text
        index (int): The question index
    """
    with open(f"quiz_scarping.md", "a", encoding="utf-8") as file:
        file.write(f"#### Question {index}\n\n")
        file.write(f"{question_text}\n\n")
        file.write(f"**Answer: {most_voted_answer} ({answer_text})**\n\n")


def q_and_a_scraping(exam_id, question_index, test: bool = False):
    if test:
        # Load local HTML file for testing
        with open(
            "test_page/Exam Associate Cloud Engineer topic 1 question 123 discussion - ExamTopics.html",
            "r",
        ) as file:
            page = file.read()
    else:
        answer_url = get_answer_url(exam_id, question_index)
        print("Answer URL:", answer_url)
        page = requests.get(answer_url, timeout=5).content

    if test or answer_url:
        try:
            soup = BeautifulSoup(page, "html.parser")
            question_text = get_question_text(soup)
            answer_text = get_answer_text(soup)
            most_voted_answer = get_most_voted_answer_text(soup)

            write_markdown_file(
                question_text,
                answer_text,
                most_voted_answer,
                question_index,
            )

        except Exception as e:
            print(f"Error saving question {question_index}: {e}")
    else:
        print(f"Question {question_index} not found")


if __name__ == "__main__":
    options = prepare_parser().parse_args()

    if options.test:
        q_and_a_scraping(options.exam, 123, options.test)
    else:
        for index in range(options.start, options.end + 1):
            q_and_a_scraping(options.exam, index, options.test)
