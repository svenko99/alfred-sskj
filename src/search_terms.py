import json
import sys
import requests
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


def search_terms_in_fran(word):
    """Returns a list of search terms for the given word."""
    url = f"https://fran.si/ajax/iskanje/autocomplete?query={word}"
    response = requests.get(url).json()
    search_terms_list = response
    if search_terms := list(search_terms_list):
        return [
            {"title": search_term, "arg": search_term} for search_term in search_terms
        ]
    else:
        return [{"title": "Word not found!", "arg": "Word not found!"}]


def output_search_terms(search_terms):
    """Outputs the search terms in the Alfred json format."""
    final_result = json.dumps({"items": search_terms})
    print(final_result)


def main():
    """Gets the input word from the command line argument and outputs the search terms."""
    word = encode_word("".join(sys.argv[1:]))
    search_terms = search_terms_in_fran(word)
    output_search_terms(search_terms)


if __name__ == "__main__":
    main()
