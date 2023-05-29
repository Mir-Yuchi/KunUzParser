from bs4 import BeautifulSoup
from utils import make_soup


def get_languages(langs_get_url: str):
    soup = make_soup(langs_get_url)
    if not isinstance(soup, BeautifulSoup):
        print("Something went wrong, retry later. Error code: ", soup)
        return
    languages = soup.find("div", class_="lang_block")
    current_language ={
        "lang": langs_get_url,
        "lang_str": languages.find("div", class_="lang_current")
    }
    other_languages = languages(".lang-list .lang-block a")
    languages_list = [current_language]
    languages_list.extend(map(
        lambda links_soup: {
            "lang": links_soup["href"].split("/")[-1].split("?")[0],
            "lang_str": links_soup.text.strip()
        },
        other_languages
    ))
    return languages_list
