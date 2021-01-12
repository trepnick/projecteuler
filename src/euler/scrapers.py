import requests
from logging import getLogger
from bs4 import BeautifulSoup

log = getLogger("rich")


def get_description(problem_number):
    try:
        response = requests.get(
            f"https://projecteuler.net/minimal={problem_number}", timeout=1
        )
        page = BeautifulSoup(response.content, "html.parser")
        return page.get_text()
    except requests.exceptions.Timeout as e:
        log.warn(e)
        return ""


if __name__ == "__main__":
    print(get_description(1))
