import sys
import requests

from utils import encode_word, output_results


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


def main():
    """Gets the input word from the command line argument and outputs the search terms."""
    word = encode_word("".join(sys.argv[1:]))
    search_terms = search_terms_in_fran(word)
    print(output_results(search_terms))


if __name__ == "__main__":
    main()
