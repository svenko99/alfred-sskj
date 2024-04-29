import sys
import requests

from bs4 import BeautifulSoup

from utils import encode_word, output_results, create_alfred_item, NOT_FOUND


def get_synonyms(word):
    """Returns a list of synonyms for the given word."""
    url = f"https://sinonimi.si/search.php?word={word}"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    synonyms_find = soup.find_all("span")[1:18]
    # check if the word is not found in the dictionary
    if synonyms := [synonym.text for synonym in synonyms_find]:
        return [
            create_alfred_item(title=synonym, subtitle="", arg=synonym, word=synonym)
            for synonym in synonyms
        ]
    else:
        return NOT_FOUND


def main():
    """Gets the input word from the command line argument and outputs the synonyms."""
    ALFRED_QUERY = encode_word(" ".join(sys.argv[1:]))
    synonyms = get_synonyms(ALFRED_QUERY)
    print(output_results(synonyms))


if __name__ == "__main__":
    main()
