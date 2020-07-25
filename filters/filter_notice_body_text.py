import re

def extract(text):
    text = re.sub("<a.*</a>"," ", text)
    text = re.sub("<img.*>"," ", text)
    text = re.sub("</div>"," ", text)
    # text = re.sub("<strong>","", text)
    # text = re.sub("</strong>","", text)
    text = re.sub("<br/>","", text)
    # text = re.sub("<h3>","", text)
    text = re.sub("</h3>","</b>", text)
    text = re.sub("</li>","", text)
    text = re.sub("<li>","", text)
    text = re.sub("<ul>","", text)
    text = re.sub("</ul>","", text)
    text = re.sub("</p>","</b>", text)
    text = re.sub("<p>","<b>", text)
    # text = re.sub("<>","<b>", text)
    # text = re.sub("<b>","", text)
    # text = re.sub("</b>","", text)
    return text
