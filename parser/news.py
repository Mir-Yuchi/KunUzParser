from urllib.parse import urljoin

from config import SITE_URL
from utils import make_soup


def parse_news(url: str) -> list:
    soup = make_soup(url)
    news = []
    news_block = soup.find(class_="top-news")
    top = news_block.find(class_="top-news__big").find("a")
    news.append({
        "link": urljoin(SITE_URL, top["href"]),
        "title": top.find(class_="big-news__title").text,
    })
    other_news = soup.select(".top-news__small-items .row .col-md-6")
    for new in other_news:
        news.append({
            "link": urljoin(SITE_URL, new.div.a["href"]),
            "preview_link": new.div.a.img["src"],
            "title": new.div.div.a.text,
        })
    return news


def parse_exact_news(url: str) -> dict:
    soup = make_soup(url)
    news_description_list = soup.find_all("p", attrs={"dir": "auto"})
    full_description = ''
    for news_desc_obj in news_description_list:
        full_description += " " + news_desc_obj.text.strip()
    return {
        "created_date": soup.find(class_="date").text,
        "views_count": soup.find(class_="view").text,
        "title": soup.find(class_="single-header__title").text,
        "short_description": soup.select(".single-content h4")[0].text,
        "full_description": full_description
    }
