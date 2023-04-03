import json
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def encode_word(word):
    """Encodes the word to URL-encoded format and changes the encoding for č, š and ž."""
    new_word = quote_plus(word)
    for old, new in [
        ["c%CC%8C", "%C4%8D"],
        ["z%CC%8C", "%C5%BE"],
        ["s%CC%8C", "%C5%A1"],
    ]:
        new_word = new_word.replace(old, new)

    return new_word


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


def output_synonyms(synonyms):
    """Outputs the synonyms in the Alfred json format."""
    final_result = json.dumps({"items": synonyms})
    print(final_result)


def main():
    """Gets the input word from the command line argument and outputs the synonyms."""
    word = encode_word("".join(sys.argv[1:]))
    synonyms = get_synonyms(word)
    output_synonyms(synonyms)


if __name__ == "__main__":
    main()
