import sys
import requests

from utils import encode_word, output_results, create_alfred_item, NOT_FOUND


def search_terms_in_fran(word):
    """Returns a list of search terms for the given word."""
    url = f"https://fran.si/ajax/iskanje/autocomplete?query={word}&dictionaries=133"
    response = requests.get(url).json()
    search_terms_list = response
    if search_terms := list(search_terms_list):
        return [
            create_alfred_item(search_term, "", search_term)
            for search_term in search_terms
        ]
    else:
        return NOT_FOUND


def main():
    """Gets the input word from the command line argument and outputs the search terms."""
    ALFRED_QUERY = encode_word(" ".join(sys.argv[1:]))
    search_terms = search_terms_in_fran(ALFRED_QUERY)
    print(output_results(search_terms))


if __name__ == "__main__":
    main()
