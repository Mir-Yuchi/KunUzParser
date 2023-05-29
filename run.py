from parser.runner.news_run import news_action_runner
from config import SITE_URL
from parser.languages import get_languages
from utils import menu_view


def run():
    actions = {
        1: {"title": f"Новости из сайта: {SITE_URL}", "action": news_action_runner},
    }
    langs = get_languages(SITE_URL)
    text = menu_view(lambda t_obj: f'{t_obj[0]}: {t_obj[-1]["lang_str"]}', langs)
    lang_index = int(input(f"Choose a language\n"
                           f"{text}\nEnter: ")) - 1
    chosen_lang = langs[lang_index]["lang"]
    text = '\n'.join(map(
        lambda command_obj: f"{command_obj[0]}: {command_obj[-1]['title']}",
        actions.items()
    ))
    command = int(input(f"Available commands:\n"
                        f"{text}\n"
                        f"Enter: "))
    actions[command]["action"](
        SITE_URL + chosen_lang if lang_index != 0 else SITE_URL
    )


if __name__ == "__main__":
    run()
