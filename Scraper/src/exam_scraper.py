import requests
from bs4 import BeautifulSoup
from googlesearch import search


class ExamScraper:
    """Class to scrape exam questions and answers from the web."""

    EXAM = {
        "gcp-ace": {
            "query": "examtopic gcp ace question",
            "keyword": "associate-cloud-engineer-topic-1-question",
        },
    }

    def __init__(self, exam_id: str) -> None:
        self.exam_id = exam_id

    def __get_answer_url(self, question_index: int) -> str | None:
        """
        Retrieve the URL for the answer page of a given question.

        Args:
            question_index (int): The index of the question

        Returns:
            str | None: The URL of the answer page or None if not found
        """
        query = f"{self.EXAM[self.exam_id]['query']} {question_index}"
        for url in search(query, sleep_interval=1):
            if f"{self.EXAM[self.exam_id]['keyword']}-{question_index}" in url:
                print(f"Found URL for question #{question_index}: {url}")
                return url
        return None

    def get_page(self, question_index: int) -> BeautifulSoup:
        """Return the parsed HTML page."""
        url = self.__get_answer_url(question_index)
        page = requests.get(url, timeout=5).content
        return BeautifulSoup(page, "html.parser")

    @staticmethod
    def get_question_text(soup: BeautifulSoup) -> tuple[str, dict]:
        """Extract the question text and choices from the parsed HTML."""
        question_body = soup.find("div", class_="question-body")
        question_text = (
            question_body.find(
                "p",
                class_="card-text",
            )
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

        choices = {
            choice.find("span", class_="multi-choice-letter")
            .get_text()
            .strip(): choice.get_text(separator=" ", strip=True)
            for choice in choices
        }
        return question_text, choices

    @staticmethod
    def get_answer_text(soup: BeautifulSoup) -> str:
        """
        Retrieve the correct answer from the parsed HTML.

        Example:
            <span class="correct-answer-box"><strong>Suggested Answer:</strong>
                <span class="correct-answer">D</span>
                <a href="#" class="vote-answer-button ml-1 d-print-none" data-toggle="tooltip" title="" data-original-title="Vote an answer">🗳️</a>
                <br>
            </span>

        Returns:
            str: The answer text
        """
        return (
            soup.find(
                "span",
                class_="correct-answer",
            )
            .get_text()
            .strip()
        )

    @staticmethod
    def get_most_voted_answer_text(soup: BeautifulSoup) -> str:
        """
        Retrieve the correct answer from the parsed HTML.

        Example:
            <div class="progress vote-distribution-bar">
                <div class="vote-bar progress-bar bg-primary" data-toggle="tooltip" role="progressbar" style="width: 94%; display: flex;" aria-valuenow="15" aria-valuemin="0" aria-valuemax="100" data-original-title="16 votes." title="">B (94%)</div>
                <div class="vote-bar progress-bar bg-info" data-toggle="tooltip" role="progressbar" style="width: 6%; display: flex;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" data-original-title="1 votes." title="">6%</div>
                <div class="vote-bar progress-bar bg-success" data-toggle="tooltip" role="progressbar" style="width: 25%; display: none;" aria-valuenow="30" aria-valuemin="0" aria-valuemax="100" data-original-title="" title="">B (20%)</div>
                <div class="vote-bar progress-bar bg-warning" data-toggle="tooltip" role="progressbar" style="width: 15%; display: none;" aria-valuenow="20" aria-valuemin="0" aria-valuemax="100" data-original-title="" title="">Other</div>
            </div>

        Returns:
            str: The most voted answer text
        """
        return (
            soup.find("div", class_="progress vote-distribution-bar")
            .find("div", class_="vote-bar")
            .get_text()
            .strip()
        )
