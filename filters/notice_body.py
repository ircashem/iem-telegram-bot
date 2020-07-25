from bs4 import BeautifulSoup
import requests
from filters.filter_notice_body_text import extract

def extract_notice_body(url):
    tmp = {}
    r = requests.get(url= url)
    soup = BeautifulSoup(r.text,features="html.parser")
    div_card_body = soup.findAll("div", {"class": "card-body"})
    count = 0
    flag = 0
    for item in div_card_body:
        card_body = str(item).split('<div class="card-body">')
        new_card_body = ''
        for i in card_body:
            new_card_body += str(i)
        tags = ['a','img']
        soup = BeautifulSoup(new_card_body, features='html.parser').find_all()
        msg  = extract(new_card_body)
        for tag in soup:
            if tag.name in tags:
                if tag.name == 'a':
                    href_link = tag.get("href")
                    link = "https://iemgroup.s3.amazonaws.com/uploads/2017/04/1234567116.pdf"
                    msg += href_link + "\n"
                    if href_link == link:
                        flag = 1
                        break
                elif tag.name == 'img':
                    if "resize" not in str(tag.get("src")):
                        msg += "\n" + href_link  
                else:
                    continue
        if flag == 1 :
            break
        msg = msg.strip("\n\n")
        msg = msg.replace("\n \n","\n")
        tmp[str(count)] = msg
        count += 1
    return tmp
