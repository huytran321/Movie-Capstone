import requests #pip install requests
from bs4 import BeautifulSoup #pip install bs4

url = 'https://pro.imdb.com/title/tt6146586/boxoffice'

def boxOfficeDataCollection():
    response = requests.get(url)
    html = response.text

    soup = BeautifulSoup(html, 'html.parser')
    