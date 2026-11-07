# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///

from concurrent.futures import ThreadPoolExecutor

import requests
from bs4 import BeautifulSoup


class CJVT:
    SEARCH_URL = "https://viri.cjvt.si/sloleks/ajax_api/v1/slv/search_exact/{word}"
    HEADWORD_URL = "https://viri.cjvt.si/sloleks/slv/headword/{id}/"

    def headword_url(self, id: int) -> str:
        """Returns the Sloleks URL of a headword with the given ID."""
        return self.HEADWORD_URL.format(id=id)

    def search(self, word: str) -> list[dict]:
        """Returns a list of Sloleks entries that exactly match word. If there are no matches, it returns an empty list."""
        response = requests.get(self.SEARCH_URL.format(word=word))

        return response.json()

    def description(self, id: int) -> str:
        """Returns the description of a headword (e.g. "samostalnik, občno ime, moški spol"). If it is missing, it returns an empty string."""
        response = requests.get(self.headword_url(id))

        soup = BeautifulSoup(response.text, "html.parser")

        description = soup.find("span", {"id": "headwordDescription"})
        return description.text.strip() if description else ""

    def data(self, word: str) -> list[dict[str, str]]:
        """Returns a list of entries with the lemma, description (word type, gender, ...) and URL for each match of word. If the word is not found, it returns an empty list."""
        entries = self.search(word)

        # Each description is a separate page request, so fetch them in parallel
        with ThreadPoolExecutor() as executor:
            descriptions = executor.map(
                self.description, (entry["id"] for entry in entries)
            )

        return [
            {
                "lemma": entry["lemma"],
                "description": description,
                "url": self.headword_url(entry["id"]),
            }
            for entry, description in zip(entries, descriptions)
        ]
