from bs4 import BeautifulSoup
import requests
from ics import Calendar
import datetime


def get_html(url):
    response = requests.get(url)
    return response.text


def parse(html):
    soup = BeautifulSoup(html, features="html.parser")
    table = soup.find('table', class_='info-table')
    tds = table.find_all('td', width="33%")
    countrys = []
    for td in tds:
        countrys.append(td.a.text)
    return countrys


def get_holidays(country):
    url = 'https://www.officeholidays.com/ics/ics_country.php?tbl_country=' + str(country).strip()
    holidays = []
    c = Calendar(requests.get(url).text)
    for i in c.events:
        holidays.append([i.name, str(i._begin)])

    return holidays


def get_countrys():
    url = 'https://www.officeholidays.com/countries/index.php'
    countrys = parse(get_html(url))
    return countrys
