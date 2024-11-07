# Imports

import re
from bs4 import BeautifulSoup
import requests
from requests import Session
import pytest

# Functions

def get_cookie() -> requests.cookies.RequestsCookieJar:
    '''
    Simple function to get cookie from API.
    '''
    root_url = 'https://country-leaders.onrender.com'
    cookie_url = '/cookie'
    req = requests.get(f"{root_url}{cookie_url}")
    return req.cookies

def get_first_paragraph(wikipedia_url: str, leader_birth_year: str, session: Session) -> str:
    '''
    Function to scrape the first paragraph containing a year from supplied Wikipedia link.

    :param wikipedia_url: String containing link to be scraped.
    :param leader_birth_year: String containing birth year to be searched for in the paragraphs.
    :param session: requests.Session() object
    :return: String with text of the first paragraph containing supplied birth year.
    '''
    print(wikipedia_url)
    leader_wiki = session.get(wikipedia_url).content
    soup = BeautifulSoup(leader_wiki, features="html.parser")
    paragraphs = soup.find_all("p")
    regex_reference = r'\[[0-9a-z]{1,2}\]'
    regex_phonetic_french = r'\(.*?Écouter.?\)'
    regex_phonetic_dutch = r'\(.*?uitspraak.*?\)'
    regex_phonetic_english = r'\(.*?;\s?.*;\s?'

    for paragraph in paragraphs:
        if re.findall(leader_birth_year, paragraph.text):
            first_regex = re.sub(regex_reference, '', paragraph.text)
            second_regex = re.sub(regex_phonetic_french, '', first_regex)
            third_regex = re.sub(regex_phonetic_dutch, '', second_regex)
            fourth_regex = re.sub(regex_phonetic_english, '(', third_regex)
    return fourth_regex

def get_leaders() -> dict[str, list[dict[str, str]]]:
    '''
    Function querying API for country list, and leaders per country. 
    
    :return: Creates a dictionary of lists of leaders, per country, and adds first paragraph of Wikipedia link containing leader birth year.
    '''
    root_url = 'https://country-leaders.onrender.com'
    cookie_url = '/cookie'
    countries_url = '/countries'
    leaders_url = '/leaders'

    session = requests.Session()
    session.get(f"{root_url}{cookie_url}")
    countries = session.get(f"{root_url}{countries_url}").json()

    leaders_per_country = dict()
    for country in countries:
        params = {'country':country, 'accept':'application/json'}
        if session.get(f"{root_url}{leaders_url}", params= params).status_code == 403:
            session.get(f"{root_url}{cookie_url}")
        leaders = session.get(f"{root_url}{leaders_url}", params= params).json()
        leaders_per_country[country] = leaders
        for index, leader in enumerate(leaders):
            if not isinstance(leader['birth_date'], str):
                continue
            else:
                leader_wiki_url = leader['wikipedia_url']
                leader_birth_year = leader['birth_date'][:4]
                first_paragraph = get_first_paragraph(leader_wiki_url, leader_birth_year, session)
                leaders_per_country[country][index]['bio'] = first_paragraph

          
    return leaders_per_country

# Testing functions

@pytest.fixture
def init_session():
    return requests.Session()

def test_get_first_paragraph(init_session):
    assert get_first_paragraph('https://en.wikipedia.org/wiki/Bill_Clinton', '1946', init_session) == 'William Jefferson  Clinton (né Blythe; born August 19, 1946) is an American lawyer and politician  who served as the 42nd president of the United States from 1993 to 2001. A member of the Democratic Party, he previously served as governor of Arkansas from 1979 to 1981 and again from 1983 to 1992. Clinton, whose policies reflected a centrist "Third Way" political philosophy, became known as a New Democrat.'
    assert get_first_paragraph('https://nl.wikipedia.org/wiki/Henri_Carton_de_Wiart', '1869', init_session) == 'Henri Victor Marie Ghislain graaf Carton de Wiart (Brussel, 31 januari 1869 – Ukkel, 6 mei 1951) (ook als "Henry" vermeld) was een Belgische politicus. Hij was Eerste Minister van 1920 tot 1921.'
    assert get_first_paragraph('https://ar.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%A7%D9%84%D8%AE%D8%A7%D9%85%D8%B3_%D8%A8%D9%86_%D9%8A%D9%88%D8%B3%D9%81', '1909', init_session ) == 'محمد الخامس بن يوسف بن الحسن بن محمد بن عبد الرحمن بن هشام بن محمد بن عبد الله بن إسماعيل بن إسماعيل بن الشريف بن علي العلوي وُلد (1327 هـ / 10 أغسطس 1909م بالقصر السلطاني بفاس)  وتوفي (1381 هـ / 26 فبراير 1961م بالرباط) خَلَف والده السلطان مولاي يوسف الذي توفي بُكرة يوم الخميس 22 جمادى الأولى سنة 1346 هـ موافق 17 نوفمبر سنة 1927م فبويع ابنه سيدي محمد سلطانا للمغرب في اليوم الموالي بعد صلاة الجمعة 23 جمادى الأولى سنة 1346 هـ موافق 18 نوفمبر سنة 1927م في القصر السلطاني بفاس  ولم يزل سلطان المغرب إلى سنة 1957م، قضى منها المنفى بين (1953-1955)، ثم اتخذ لقب الملك سنة 1957م ولم يزل ملكا إلى وفاته سنة 1961م، ساند السلطان محمد الخامس نضالات الحركة الوطنية المغربية المطالبة بتحقيق الاستقلال، الشيء الذي دفعه إلى الاصطدام بسلطات الحماية. وكانت النتيجة قيام سلطات الحماية بنفيه إلى مدغشقر. وعلى إثر ذلك اندلعت مظاهرات مطالبة بعودته إلى وطنه. وأمام اشتداد حدة المظاهرات، قبلت السلطات الفرنسية بإرجاع السلطان إلى عرشه يوم 16 نوفمبر 1955. وبعد بضعة شهور تم إعلان استقلال المغرب. كان الملك محمد الخامس يكنى: أبا عبد الله.'
    assert get_first_paragraph('https://fr.wikipedia.org/wiki/Nicolas_Sarkozy', '1955', init_session) == "Nicolas Sarközy de Nagy-Bocsa, dit Nicolas Sarkozy , né le 28 janvier 1955 à Paris (France), est un homme d'État français. Il est président de la République française du 16 mai 2007 au 15 mai 2012."

@pytest.mark.xfail
def fail_test_first_paragraph(init_session):
    assert type(get_first_paragraph('https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%82%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87', '1952', init_session)) == None
    assert get_first_paragraph('https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%82%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87', '1952', init_session) == ''

def test_get_leaders():
    assert type(get_leaders()) == dict
    assert get_leaders()['us'][0]['first_name'] == 'George'

# Running tests if main 

if __name__ == "__main__":
    pytest.main(['-v'])