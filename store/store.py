from bs4 import BeautifulSoup
import requests
import os

class Store :
    def __init__(self, name,URL) :
        self.name = name
        self.URL = URL

    def request(self,BOOK_ISBN):
        BOOK_URL = self.URL + BOOK_ISBN
        print(BOOK_URL)
        headers = {
        'User-Agent': os.getenv("USER_AGENT")
        }
        req = requests.get(BOOK_URL ,headers=headers)
        if req.status_code >= 400 :
            print(self.name,"store doesn't have ISBN:",BOOK_ISBN,"book")
            return
        return BeautifulSoup(req.content ,features="html.parser")

