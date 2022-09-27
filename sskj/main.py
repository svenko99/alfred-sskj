import json
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import quote_plus

# Get word from query and encode it to URL-encoded format
beseda = sys.argv[1]
nova = quote_plus(beseda)

# Change URL-encoded formats of ("č", "š", "ž") chars because alfred encodes it weirdly
for old, new in [["c%CC%8C", "%C4%8D"], ["z%CC%8C", "%C5%BE"], ["s%CC%8C", "%C5%A1"]]:
    nova = nova.replace(old, new)

# Get response from website fran.si and convert it to soup object
f = f"https://fran.si/iskanje?View=1&Query={nova}"
response = requests.get(f)
soup = BeautifulSoup(response.content, "html.parser")

# Find all definitions
use_razlage = soup.find_all(
    "span", {"data-placement": "top", "data-group": "explanation "}
)

# Find all headers of word with diffrent definitions
use_glava = soup.find_all("span", {"data-group": "header"})

# Append all headers and definitions to list so it can be used as JSON to output to alfred
sez = [
    {
        "title": f"{beseda} {glavica.text}",
        "arg": razlagica.text[:-1],
        "subtitle": razlagica.text[:-1],
    }
    for glavica, razlagica in zip(use_glava, use_razlage)
]

# Output result to alfred
final_result = json.dumps({"items": sez})

# Check if word exist in SSKJ, if not display "Word not found!"
if sez:
    print(final_result)
else:
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
