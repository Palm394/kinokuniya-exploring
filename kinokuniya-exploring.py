#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os

load_dotenv()

URL = os.getenv("URL")
headers = {
    'User-Agent': os.getenv("USER_AGENT")
}
req = requests.get(URL ,headers=headers)
soup = BeautifulSoup(req.content ,features="html.parser")

#find title name of the book
print(soup.find("h1").string)

#find stock status
stock_status = str(soup.find("div", class_="stock").h2.span.string)
print(stock_status.strip())
