import re

def extract_news_text(text):
    text = re.sub('<a.*">', "", text)
    text = re.sub('</a>', '', text)
    text = re.sub('</h1>', '', text)
    text = re.sub('<hr/>', '', text)
    text = re.sub('</p>', '</b>', text)
    text = re.sub('<p>', '<b>', text)
    text = re.sub('</div>', '', text)
    return text