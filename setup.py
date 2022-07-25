#!/usr/bin/env python3
from ./store/kinokuniya import kinokuniya
from dotenv import load_dotenv
import os

print("Hello bookComp")

load_dotenv()
BOOK_ISBN_LIST = os.getenv("BOOK_ISBN").split(",")

for isbn in BOOK_ISBN_LIST:
    kinokuniya.find_a_book(isbn)