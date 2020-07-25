from bs4 import BeautifulSoup
import requests 

def extract_notice_header(url):
    r = requests.get(url= url)
    # print(r.text)
    tmp = []
    soup = BeautifulSoup(r.text,features="html.parser")
    div_card_header = soup.findAll("div", {"class": "card-header"})
    # div_card_body = soup.findAll("div", {"class": "card-body"})
    for item in div_card_header:
        item = str(item).split("<br/>")
        item = item[1].strip("\n")
        if "</a></h5>\n</div>" in item:
            item = item.split("</a>")[0]
        tmp.append(item)
    return tmp

