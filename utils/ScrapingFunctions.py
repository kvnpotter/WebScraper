# Imports

import re
from bs4 import BeautifulSoup
import requests
from requests import Session
import pytest

# Functions


def get_cookie() -> requests.cookies.RequestsCookieJar:
    """
    Simple function to get cookie from API.
    """
    root_url = "https://country-leaders.onrender.com"
    cookie_url = "/cookie"
    req = requests.get(f"{root_url}{cookie_url}")
    return req.cookies


def get_first_paragraph(
    wikipedia_url: str, leader_birth_year: str, session: Session
) -> str:
    """
    Function to scrape the first paragraph containing a year from supplied Wikipedia link.

    :param wikipedia_url: String containing link to be scraped.
    :param leader_birth_year: String containing birth year to be searched for in the paragraphs.
    :param session: requests.Session() object
    :return: String with text of the first paragraph containing supplied birth year.
    """
    print(wikipedia_url)
    leader_wiki = session.get(wikipedia_url).content
    soup = BeautifulSoup(leader_wiki, features="html.parser")
    paragraphs = soup.find_all("p")
    regex_reference = r"\[[0-9a-z]{1,2}\]"
    regex_phonetic_french = r"\(.*?Écouter.?\)"
    regex_phonetic_dutch = r"\(.*?uitspraak.*?\)"
    regex_phonetic_english = r"\(.*?;\s?.*;\s?"

    for paragraph in paragraphs:
        if re.findall(leader_birth_year, paragraph.text):
            first_regex = re.sub(regex_reference, '', paragraph.text)
            second_regex = re.sub(regex_phonetic_french, '', first_regex)
            third_regex = re.sub(regex_phonetic_dutch, '', second_regex)
            fourth_regex = re.sub(regex_phonetic_english, '(', third_regex)
            break
    return fourth_regex


def get_leaders() -> dict[str, list[dict[str, str]]]:
    """
    Function querying API for country list, and leaders per country.

    :return: Creates a dictionary of lists of leaders, per country, and adds first paragraph of Wikipedia link containing leader birth year.
    """
    root_url = "https://country-leaders.onrender.com"
    cookie_url = "/cookie"
    countries_url = "/countries"
    leaders_url = "/leaders"

    session = requests.Session()
    session.get(f"{root_url}{cookie_url}")
    countries = session.get(f"{root_url}{countries_url}").json()

    leaders_per_country = dict()
    for country in countries:
        params = {"country": country, "accept": "application/json"}
        if session.get(f"{root_url}{leaders_url}", params=params).status_code == 403:
            session.get(f"{root_url}{cookie_url}")
        leaders = session.get(f"{root_url}{leaders_url}", params=params).json()
        leaders_per_country[country] = leaders
        for index, leader in enumerate(leaders):
            if not isinstance(leader["birth_date"], str):
                continue
            else:
                leader_wiki_url = leader["wikipedia_url"]
                leader_birth_year = leader["birth_date"][:4]
                first_paragraph = get_first_paragraph(
                    leader_wiki_url, leader_birth_year, session
                )
                leaders_per_country[country][index]["bio"] = first_paragraph

    return leaders_per_country


# Running tests if main

if __name__ == "__main__":
    pytest.main(["./test_ScrapingFunctions.py", "-v"])
