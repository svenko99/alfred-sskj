import sys
import http.client

from bs4 import BeautifulSoup

from utils import output_results, create_alfred_item, encode_word, quote_word


def get_word_definitions(word):
    """Returns a list of definitions for the given word."""
    link = f"https://fran.si/iskanje?FilteredDictionaryIds=133&View=1&Query={word}"
    conn = http.client.HTTPSConnection("fran.si")
    conn.request(
        "GET", f"/iskanje?FilteredDictionaryIds=133&View=1&Query={quote_word(word)}"
    )
    res = conn.getresponse()
    data = res.read()
    soup = BeautifulSoup(data, "html.parser")
    explenaitions = soup.find_all("span", {"data-group": "explanation "})
    results = []

    if explenaitions:
        for expl in explenaitions:
            expl = expl.text.strip()[:-1]
            results.append(
                create_alfred_item(title=expl, subtitle=expl, arg=expl, word=word)
            )

    elif explenaitions := soup.find_all("a", {"class": "reference"}):
        for expl in explenaitions:
            expl = expl.text.strip()
            results.append(create_alfred_item(expl, expl, expl, link))

    return results or [
        {
            "title": "Word not found",
            "subtitle": "Click to open search query in fran.si",
            "arg": link,
        }
    ]


def main():
    """Gets the input word from the Alfred and outputs the definitions."""
    ALFRED_QUERY = encode_word(" ".join(sys.argv[1:]))
    definitions = get_word_definitions(ALFRED_QUERY)
    print(output_results(definitions))


if __name__ == "__main__":
    main()
