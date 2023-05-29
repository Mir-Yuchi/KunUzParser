from typing import Callable, Union

import requests
from bs4 import BeautifulSoup


def make_soup(url: str, **params) -> BeautifulSoup | int:
    response = requests.get(url, **params)
    if response.status_code != 200:
        return response.status_code
    return BeautifulSoup(response.text, "html.parser")


def menu_view(handler: Callable, source_list: Union[list, tuple, set]) -> str:
    return 'n'.join(map(
        handler,
        enumerate(source_list, start=1)
    ))
