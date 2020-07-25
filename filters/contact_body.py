import requests
from bs4 import BeautifulSoup
from filters.filter_notice_body_text import extract

def extract_contact(url):
    data = []
    r = requests.get(url= url)
    soup = BeautifulSoup(r.text, features='html.parser')
    tmp = str(soup.find_all("div", {"class":"col-md-8"})[-1])
    contact_header = tmp.split('<h3 class="heading-border-bottom">')[1:]
    for item in contact_header:
        data.append(extract(item))
    return data
