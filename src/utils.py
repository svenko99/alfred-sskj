from urllib.parse import quote_plus
import json


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


def output_results(results):
    """Outputs the results in the Alfred json format."""
    return json.dumps({"items": results})
