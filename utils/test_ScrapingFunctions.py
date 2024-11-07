import re
from bs4 import BeautifulSoup
import requests
from requests import Session
import pytest
from ScrapingFunctions import get_cookie, get_first_paragraph, get_leaders

# Testing functions

@pytest.fixture
def init_session():
    return requests.Session()

def test_get_first_paragraph(init_session):
    assert get_first_paragraph('https://nl.wikipedia.org/wiki/Henri_Carton_de_Wiart', '1869', init_session) == 'Henri Victor Marie Ghislain graaf Carton de Wiart (Brussel, 31 januari 1869 – Ukkel, 6 mei 1951) (ook als "Henry" vermeld) was een Belgische politicus. Hij was Eerste Minister van 1920 tot 1921.\n'
    assert get_first_paragraph('https://ar.wikipedia.org/wiki/%D9%85%D8%AD%D9%85%D8%AF_%D8%A7%D9%84%D8%AE%D8%A7%D9%85%D8%B3_%D8%A8%D9%86_%D9%8A%D9%88%D8%B3%D9%81', '1909', init_session ) == 'محمد الخامس بن يوسف بن الحسن بن محمد بن عبد الرحمن بن هشام بن محمد بن عبد الله بن إسماعيل بن إسماعيل بن الشريف بن علي العلوي وُلد (1327 هـ / 10 أغسطس 1909م بالقصر السلطاني بفاس)  وتوفي (1381 هـ / 26 فبراير 1961م بالرباط) خَلَف والده السلطان مولاي يوسف الذي توفي بُكرة يوم الخميس 22 جمادى الأولى سنة 1346 هـ موافق 17 نوفمبر سنة 1927م فبويع ابنه سيدي محمد سلطانا للمغرب في اليوم الموالي بعد صلاة الجمعة 23 جمادى الأولى سنة 1346 هـ موافق 18 نوفمبر سنة 1927م في القصر السلطاني بفاس  ولم يزل سلطان المغرب إلى سنة 1957م، قضى منها المنفى بين (1953-1955)، ثم اتخذ لقب الملك سنة 1957م ولم يزل ملكا إلى وفاته سنة 1961م، ساند السلطان محمد الخامس نضالات الحركة الوطنية المغربية المطالبة بتحقيق الاستقلال، الشيء الذي دفعه إلى الاصطدام بسلطات الحماية. وكانت النتيجة قيام سلطات الحماية بنفيه إلى مدغشقر. وعلى إثر ذلك اندلعت مظاهرات مطالبة بعودته إلى وطنه. وأمام اشتداد حدة المظاهرات، قبلت السلطات الفرنسية بإرجاع السلطان إلى عرشه يوم 16 نوفمبر 1955. وبعد بضعة شهور تم إعلان استقلال المغرب. كان الملك محمد الخامس يكنى: أبا عبد الله.\n'
    assert get_first_paragraph('https://fr.wikipedia.org/wiki/Nicolas_Sarkozy', '1955', init_session) == "Nicolas Sarközy de Nagy-Bocsa, dit Nicolas Sarkozy , né le 28 janvier 1955 à Paris (France), est un homme d'État français. Il est président de la République française du 16 mai 2007 au 15 mai 2012.\n"

@pytest.mark.xfail
def test_first_paragraph_fail(init_session):
    assert type(get_first_paragraph('https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%82%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87', '1952', init_session)) == None
    assert get_first_paragraph('https://ru.wikipedia.org/wiki/%D0%9F%D1%83%D1%82%D0%B8%D0%BD,_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80_%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87', '1952', init_session) == ''

#def test_get_leaders():
    #assert type(get_leaders()) == dict
    #assert get_leaders()['us'][0]['first_name'] == 'George'