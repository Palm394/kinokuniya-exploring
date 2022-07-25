from store import Store

#Initialize store from class
Kinokuniya = Store("kinokuniya","https://thailand.kinokuniya.com/bw/")

#request a book
soup = Kinokuniya.request(BOOK_ISBN="9781032340104")

#find title name of the book
print(soup.find("h1").string)

#find stock status
stock_status = str(soup.find("div", class_="stock").h2.span.string)
print(stock_status.strip())
price = str(soup.find("li", class_="price").span.string)
print(price)
print('--------------------')