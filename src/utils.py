import json
import unicodedata
from urllib.parse import quote

# Constants
NOT_FOUND = [{"title": "Word not found", "arg": "Word not found"}]


def output_results(results):
    """Outputs the results in the Alfred json format."""
    return json.dumps({"items": results})


def create_alfred_item(
    title, subtitle=None, arg=None, quicklookurl=None, word=None, is_fran=True, mod=None
):
    """Returns a dictionary with the given parameters."""
    return {
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "quicklookurl": quicklookurl,
        "mods": {
            "alt": {
                "valid": True,
                "arg": (
                    f"https://fran.si/iskanje?FilteredDictionaryIds=133&View=1&Query={word}"
                    if is_fran
                    else mod
                ),
                "subtitle": "Open in browser (⌥ + ↩)",
            }
        },
    }


def encode_word(word):
    """Encodes the word to utf-8."""
    return unicodedata.normalize("NFC", word.strip())


def quote_word(word):
    """Quotes the word."""
    return quote(word)
