# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///

import requests
from bs4 import BeautifulSoup


class SSKJ:
    DEFINITION_URL = "https://fran.si/iskanje"
    SEARCH_URL = "https://fran.si/ajax/iskanje/autocomplete"
    DEFINITION_DICTIONARY_ID = 133  # ID for Fran's SSKJ^2 dictionary
    SYNONYM_DICTIONARY_ID = 208  # ID for Fran's Sinonimni dictionary

    def search(self, query: str) -> list[str]:
        """Returns a list of words that match query. If there are no matches, it returns an empty list."""
        response = requests.get(
            self.SEARCH_URL,
            params={"query": query, "dictionaries": self.DEFINITION_DICTIONARY_ID},
        )

        return response.json()

    def definition(self, word: str) -> list[str]:
        """Returns a list of different word definitions. If the word is not found, it returns an empty list."""
        response = requests.get(
            self.DEFINITION_URL,
            params={
                "Query": word,
                "FilteredDictionaryIds": self.DEFINITION_DICTIONARY_ID,
                "View": 1,
            },
        )

        soup = BeautifulSoup(response.text, "html.parser")

        # The last [:-1] character of the text is ":" and hence removed
        return [
            el.text[:-1] for el in soup.find_all("span", {"data-group": "explanation "})
        ]

    def synonym(self, word: str) -> list[str]:
        """Returns a list of synonyms for a given word. If the word is not found or has no synonyms, it returns an empty list."""
        response = requests.get(
            self.DEFINITION_URL,
            params={
                "Query": word,
                "FilteredDictionaryIds": self.SYNONYM_DICTIONARY_ID,
                "View": 1,
            },
        )

        soup = BeautifulSoup(response.text, "html.parser")

        words = []
        for label in soup.find_all("span", string="SINONIMI:"):
            synonyms_box = label.parent.find_next_sibling(
                "div"
            )  # Div with links next to the label
            for link in synonyms_box.find_all("a", class_="reference"):
                word = link.find(
                    string=True, recursive=False
                ).strip()  # Skip <sup>1</sup>
                if word not in words:  # Skip duplicates, keep original order
                    words.append(word)

        return words
