import sys
import requests
from bs4 import BeautifulSoup

from utils import encode_word, output_results


def get_synonyms(word):
    """Returns a list of synonyms for the given word."""
    url = f"https://sinonimi.si/search.php?word={word}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    synonyms_find = soup.find_all("span")[1:18]
    # check if the word is not found in the dictionary
    if synonyms := [synonym.text for synonym in synonyms_find]:
        return [{"title": synonym, "arg": synonym} for synonym in synonyms]
    else:
        return [{"title": "Word not found!", "arg": "Word not found!"}]


def main():
    """Gets the input word from the command line argument and outputs the synonyms."""
    word = encode_word("".join(sys.argv[1:]))
    synonyms = get_synonyms(word)
    print(output_results(synonyms))


if __name__ == "__main__":
    main()
