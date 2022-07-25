#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BOOK_ISBN_LIST = os.getenv("BOOK_ISBN").split(",")

def find_a_book(ISBN_of_a_book) :
    URL = os.getenv("URL") + ISBN_of_a_book
    headers = {
        'User-Agent': os.getenv("USER_AGENT")
    }
    req = requests.get(URL ,headers=headers)
    
    if req.status_code >= 400 :
        print("Oh! your book with ISBN:",ISBN_of_a_book,"is invalid")
        return
    
    soup = BeautifulSoup(req.content ,features="html.parser")
    #find title name of the book
    print(soup.find("h1").string)
    #find stock status
    stock_status = str(soup.find("div", class_="stock").h2.span.string)
    print(stock_status.strip())
    print('--------------------')

for isbn in BOOK_ISBN_LIST:
    find_a_book(isbn)