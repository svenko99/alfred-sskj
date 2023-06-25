import json
import unicodedata

# Constants
NOT_FOUND = [{"title": "Word not found", "arg": "Word not found"}]


def output_results(results):
    """Outputs the results in the Alfred json format."""
    return json.dumps({"items": results})


def create_alfred_item(title, subtitle=None, arg=None, quicklookurl=None):
    """Returns a dictionary with the given parameters."""
    return {
        "title": title,
        "subtitle": subtitle,
        "arg": arg,
        "quicklookurl": quicklookurl,
    }


def encode_word(word):
    """Encodes the word to utf-8."""
    return unicodedata.normalize("NFC", word.strip())
