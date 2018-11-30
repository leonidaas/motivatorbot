import requests
from bs4 import BeautifulSoup as BS
import random
import json


class Crawler:

    def __init__(self):
        print("Crawler wurde angestoßen")
        self.url = 'https://www.brainyquote.com/topics/motivational'
        self.quotes = list()
        self.source = requests.get(self.url)
        plain_text = self.source.text
        self.cid = 0
        self.counter = 1

        obj = BS(plain_text, "html5lib")

        for a in obj.find_all('a', {'title': 'view quote'}):
            #print (a.text)
            self.quotes.append(
                a.text
            )


    def getRandomQuote(self):
        quote = self.quotes[random.randint(0, len(self.quotes))]

        while len(quote) == 0:
            quote = self.quotes[random.randint(0, len(self.quotes))]

        return quote

    def fetchQuotes(self):
        print("fetching quotes..")
        self.quotes.clear()
        self.source = requests.get(self.url)
        plain_text = self.source.text

        obj = BS(plain_text, "html5lib")

        for a in obj.find_all('a', {'title': 'view quote'}):
            self.quotes.append(
                a.text
            )
        self.counter = 1

    def fetchMoreQuotes(self):
        print("scrolling down the page")
        self.api = "https://www.brainyquote.com/api/inf"

        self.data = {}
        self.data['typ'] = "topic"
        self.data['langc'] = "en"
        self.data['v'] = "8.5.4:3062111"
        self.data['ab'] = "b"
        self.data['pg'] = self.counter
        self.data['id'] = "t:132622"
        self.data['vid'] = "7b363d749b4c7c684ace871c8a75f8e6"
        self.data['fdd'] = "d"
        self.data['m'] = 0

        self.source = requests.request(method="get", url=self.api, json=self.data)
        print(self.source)
        self.counter += 1
        obj2 = BS(self.source.content, "html5lib")

        stringToSlice = str(obj2)
        finishedString = stringToSlice[50:len(obj2.text) - 16]

        soup = BS(finishedString, "html5lib")

        for a in soup.find_all('a', {'class', '\\"b-qt'}):
            self.quotes.append(
                a.text
            )



    def printAllQuotes(self):
        for q in self.quotes:
            print(q)
