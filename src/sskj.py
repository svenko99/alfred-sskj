import sys
import requests
from bs4 import BeautifulSoup

from utils import encode_word, output_results


def get_word_definitions(word):
    """Returns a list of definitions for the given word."""
    link = f"https://www.termania.net/iskanje?ld=58&query={word}&SearchIn=Linked"
    response = requests.get(link)
    soup = BeautifulSoup(response.content, "html.parser")

    # Scarp the data from the page and check if the word is not found in the dictionary:
    # It will output "Iskani niz je bil najden v DRUGI VSEBINI teh gesel"
    # which means that the word is not in the dictionary we are scraping
    try:
        if "DRUGI VSEBINI" in soup.find("h4", {"class", "normal-heading"}).text.strip():
            raise Exception
        all_definitions = soup.find("div", {"class": "list-group results"})
        definitions = [
            i.text.strip() for i in all_definitions.find_all("p", {"class": "content"})
        ]

    except Exception:
        # if the word is not found, output the error message
        return [
            {
                "title": "Word not found in Termania. - Click to search in fran.si",
                "arg": f"https://fran.si/iskanje?View=1&Query={word}",
                "subtitle": "",
            }
        ]

    # Replace the 1. and 2. etc. with "$$$" so we can split them later
    separated_definitions = ""
    for definition in definitions:
        for i in range(1, 8):
            if f"{i}." in definition:
                definition = definition.replace(f"{i}.", "$$$")
        separated_definitions += definition

    # Split the definitions in each definition
    splited_defintions = [
        i.strip() for i in separated_definitions.split("$$$") if i.strip() != ""
    ]

    # Iterate over the definitions
    result = [
        {
            "title": defnts,
            "arg": defnts,
            "subtitle": defnts,
        }
        for defnts in splited_defintions
    ]

    return result


def main():
    """Gets the input word from the Alfred and outputs the definitions."""
    word = encode_word("".join(sys.argv[1:]))
    definitions = get_word_definitions(word)
    print(output_results(definitions))


if __name__ == "__main__":
    main()
