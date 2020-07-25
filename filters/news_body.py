from bs4 import BeautifulSoup
import requests
import re
from filters.filter_news_text import extract_news_text

def extract_news(url):
    data = []
    r = requests.get(url= url)
    soup = BeautifulSoup(r.text, features='html.parser')
    tmp = str(soup.find_all('div',{"class":"col-md-8"}))
    news_body = tmp.split('<h1 class="section-header text-left">')[2:]
    for item in news_body:
        website = "https://www.iem.edu.in"
        msg = re.findall('<a\s+(?:[^>]*?\s+)?href="([^"]*)"', item)[-1]
        if "https://" not in msg:
            msg = website + msg
        msg += extract_news_text(item)
        data.append(msg)
    return data
