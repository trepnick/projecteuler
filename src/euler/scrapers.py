from logging import getLogger

import requests
from bs4 import BeautifulSoup

log = getLogger("rich")


def get_description(problem_number: int):
    try:
        response = requests.get(
            f"https://projecteuler.net/minimal={problem_number}", timeout=1
        )
        page = BeautifulSoup(response.content, "html.parser")
        return page.get_text()
    except requests.exceptions.Timeout as e:
        log.error(e)
        return ""
