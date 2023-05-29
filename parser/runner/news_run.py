from parser.news import parse_news, parse_exact_news
from utils import menu_view


def news_action_runner(url: str):
    news = parse_news(url)
    pretty_menu = menu_view(
        lambda news_tuple: f'{news_tuple[0]}: {news_tuple[-1]["title"]}',
        news
    )
    news_index = int(input(
        "Founded news:\n" + pretty_menu +
        "\nChoose news to know more\nEnter: "
    )) - 1
    news_obj = parse_exact_news(news[news_index]["link"])
    print(
        "\u001b[32m" + news_obj["created_date"] + "\u001b[32m" + f" \U0001F441 {news_obj['views_count']}",
        "\u001b[34m" + news_obj["title"],
        "\u001b[36m" + news_obj["short_description"],
        "\u001b[31m" + news_obj["full_description"],
        sep="\n"
    )
