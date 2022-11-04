import json
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus


def main(inputed_word):
    # Get the search term from the command line
    word = quote_plus(inputed_word)

    # Change URL-encoded formats of ("č", "š", "ž") chars because alfred encodes it weirdly
    for old, new in [
        ["c%CC%8C", "%C4%8D"],
        ["z%CC%8C", "%C5%BE"],
        ["s%CC%8C", "%C5%A1"],
    ]:
        word = word.replace(old, new)

    # Get the page
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
        print(
            json.dumps(
                {
                    "items": [
                        {
                            "title": "Word not found!",
                            "arg": "Word not found!",
                        }
                    ]
                }
            )
        )
        sys.exit()

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

    # Iterate over the definitions and put them in the alfred json format
    sez = [
        {
            "title": defnts,
            "arg": defnts,
            "subtitle": defnts,
        }
        for defnts in splited_defintions
    ]

    # Output result to alfred
    final_result = json.dumps({"items": sez})
    print(final_result)


if __name__ == "__main__":
    main("".join(sys.argv[1:]))
