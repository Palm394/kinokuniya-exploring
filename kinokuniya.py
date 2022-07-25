#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests
import os

def find_a_book(ISBN_of_a_book) :
    #find title name of the book
    print(soup.find("h1").string)
    
    #find stock status
    stock_status = str(soup.find("div", class_="stock").h2.span.string)
    print(stock_status.strip())
    price = str(soup.find("li", class_="price").span.string)
    print(price)
    print('--------------------')

if __name__ == "__main__" :
    print("Welcome to Kinokuniya Module!")