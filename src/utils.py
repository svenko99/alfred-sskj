from urllib.parse import quote_plus
import json

# Constants
NOT_FOUND = [{"title": "Word not found", "arg": "Word not found"}]


def encode_word(word):
    """Encodes the word to URL-encoded format and changes the encoding for č, š and ž."""
    new_word = quote_plus(word.lower())
    for old, new in [
        ["c%CC%8C", "%C4%8D"],
        ["z%CC%8C", "%C5%BE"],
        ["s%CC%8C", "%C5%A1"],
    ]:
        new_word = new_word.replace(old, new)

    return new_word


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
