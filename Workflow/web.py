"""Minimal HTTP helpers built on the standard library."""

import json
from typing import Any, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen

TIMEOUT = 10
HEADERS = {"User-Agent": "alfred-sskj"}


def get(url: str, params: Optional[dict] = None) -> str:
    """Returns the decoded body of a GET request to url with the given query params."""
    if params:
        url = f"{url}?{urlencode(params)}"
    with urlopen(Request(url, headers=HEADERS), timeout=TIMEOUT) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset)


def get_json(url: str, params: Optional[dict] = None) -> Any:
    """Returns the parsed JSON body of a GET request to url."""
    return json.loads(get(url, params))
