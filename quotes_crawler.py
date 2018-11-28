import requests
from bs4 import BeautifulSoup as BS
import random


class Crawler:

    def __init__(self):
        print("Crawler wurde angestoßen")
        self.url = 'https://www.brainyquote.com/topics/motivational'
        self.quotes = list()
        self.source = requests.get(self.url)
        plain_text = self.source.text

        obj = BS(plain_text, "html5lib")

        for a in obj.find_all('a', {'title': 'view quote'}):
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
