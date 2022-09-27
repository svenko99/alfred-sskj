import json
import sys
import requests
from bs4 import BeautifulSoup
import urllib.parse

# Get word from query and encode it to URL-encoded format
beseda = sys.argv[1]
nova = urllib.parse.quote_plus(beseda)

# Change URL-encoded formats of ("č", "š", "ž") chars because alfred encodes it weirdly
for old, new in [["c%CC%8C", "%C4%8D"], ["z%CC%8C", "%C5%BE"], ["s%CC%8C", "%C5%A1"]]:
    nova = nova.replace(old, new)

# Get response from website sininomi.si and convert it to soup object
f = f"https://sinonimi.si/search.php?word={nova}"
response = requests.get(f)
soup = BeautifulSoup(response.content, "lxml")

# Find all synonyms
all_synonyms = soup.find_all("span")


# Append all synonyms to list so it can be used as JSON to output to alfred
sez = [
    {
        "title": sininomek.text,
        "arg": sininomek.text,
    }
    for sininomek in all_synonyms[1:18]
]

# Output result to alfred
final_result = json.dumps({"items": sez})

# Check if word exist in sininomi.si, if not display "Word not found!"
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
