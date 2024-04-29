import sys
import json
import requests


from bs4 import BeautifulSoup

from utils import encode_word, output_results, create_alfred_item, NOT_FOUND


def get_id_of_word(word):
    url = f"https://viri.cjvt.si/sloleks/ajax_api/v1/slv/search_exact/{word}"
    data = requests.get(url).json()
    return data[0]["id"]


def get_data_for_word(id):
    url = f"https://viri.cjvt.si/sloleks/slv/headword/{id}/"
    data = requests.get(url).text
    soup = BeautifulSoup(data, "html.parser")
    data_for_word = soup.find("span", {"id": "headwordDescription"}).text.strip()
    return data_for_word


def main():
    word = encode_word(sys.argv[1])
    try:
        id = get_id_of_word(word)
        url = f"https://viri.cjvt.si/sloleks/slv/headword/{id}/"
        data = get_data_for_word(id)
        print(
            output_results(
                [
                    create_alfred_item(
                        f"{word} - {data}",
                        "",
                        arg=f"{word} - {data}",
                        is_fran=False,
                        mod=url,
                        quicklookurl=url,
                    )
                ]
            )
        )
    except:
        print(output_results(NOT_FOUND))


if __name__ == "__main__":
    main()
