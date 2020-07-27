import requests

def random_quote():
    try:       
        url = "https://programming-quotes-api.herokuapp.com/quotes/random"
        r = requests.get(url)
        obj = r.json()
        quote = obj["en"].strip(".") + " : " + obj['author']
        return quote
    except BaseException:
        return "This is just start of a new adventure morty, wanna be a part of it? : Rick"

