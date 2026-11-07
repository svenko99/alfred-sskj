# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "beautifulsoup4",
#     "requests",
# ]
# ///

"""Alfred script filter for SSKJ, synonyms and Sloleks word data.

Usage: alfred.py {sskj|sinonim|podatki|iskanje} <query>

Result items set an ``action`` variable (COPY or OPEN) that a Conditional
utility in the workflow routes to Copy to Clipboard or Open URL. Items from
``iskanje`` are instead connected straight to the other script filters, so
the selected word is looked up with the chosen modifier.
"""

import json
import sys
import unicodedata
from collections.abc import Callable
from typing import Any
from urllib.parse import urlencode

import requests

from cjvt import CJVT
from sskj import SSKJ

Item = dict[str, Any]

COPY = "COPY"
OPEN = "OPEN"

sskj = SSKJ()
cjvt = CJVT()


def fran_url(word: str, dictionary_id: int) -> str:
    """Returns the fran.si URL of word in the given dictionary."""
    params = {"Query": word, "FilteredDictionaryIds": dictionary_id, "View": 1}
    return f"{SSKJ.DEFINITION_URL}?{urlencode(params)}"


def result_item(title: str, url: str, subtitle: str = "", copy: str = "") -> Item:
    """Item that copies its text on ↩ and opens url on ⌥↩."""
    copy = copy or title
    return {
        "title": title,
        "subtitle": subtitle,
        "arg": copy,
        "variables": {"action": COPY},
        "quicklookurl": url,
        "text": {"copy": copy, "largetype": copy},
        "mods": {
            "alt": {
                "arg": url,
                "variables": {"action": OPEN},
                "subtitle": "Odpri v brskalniku",
            },
        },
    }


def not_found_item(url: str) -> Item:
    return {
        "title": "Beseda ni bila najdena",
        "subtitle": "↩ za iskanje v brskalniku",
        "arg": url,
        "variables": {"action": OPEN},
    }


def definitions(word: str) -> list[Item]:
    url = fran_url(word, SSKJ.DEFINITION_DICTIONARY_ID)
    return [
        # Definitions are often too long for the title, so repeat them in the subtitle
        result_item(definition, url, subtitle=definition)
        for definition in sskj.definition(word)
    ] or [not_found_item(url)]


def synonyms(word: str) -> list[Item]:
    url = fran_url(word, SSKJ.SYNONYM_DICTIONARY_ID)
    return [
        result_item(synonym, url)
        for synonym in sskj.synonym(word)
    ] or [not_found_item(url)]


def word_data(word: str) -> list[Item]:
    return [
        result_item(
            entry["description"],
            entry["url"],
            subtitle=entry["lemma"],
            copy=f"{entry['lemma']} - {entry['description']}",
        )
        for entry in cjvt.data(word)
    ] or [not_found_item(fran_url(word, SSKJ.DEFINITION_DICTIONARY_ID))]


def suggestions(query: str) -> list[Item]:
    """Words matching query. The workflow connects ↩, ⌘↩ and ⌃↩ to the sskj, sinonim and podatki script filters."""
    return [
        {
            "title": word,
            "arg": word,
            "autocomplete": word,
            "mods": {
                "cmd": {"subtitle": "Sinonimi"},
                "ctrl": {"subtitle": "Osnovni podatki o besedi"},
                "alt": {
                    "arg": fran_url(word, SSKJ.DEFINITION_DICTIONARY_ID),
                    "subtitle": "Odpri v brskalniku",
                },
            },
        }
        for word in sskj.search(query)
    ] or [{"title": "Ni zadetkov", "subtitle": query, "valid": False}]


COMMANDS: dict[str, Callable[[str], list[Item]]] = {
    "sskj": definitions,
    "sinonim": synonyms,
    "podatki": word_data,
    "iskanje": suggestions,
}


def main() -> None:
    command, *words = sys.argv[1:]
    # Alfred passes decomposed (NFD) text, the dictionaries expect composed (NFC)
    query = unicodedata.normalize("NFC", " ".join(words).strip())

    if not query:
        items = [{"title": "Vpiši besedo", "valid": False}]
    else:
        try:
            items = COMMANDS[command](query)
        except requests.RequestException as error:
            items = [
                {
                    "title": "Napaka pri povezavi",
                    "subtitle": str(error),
                    "valid": False,
                }
            ]

    print(json.dumps({"items": items}))


if __name__ == "__main__":
    main()
