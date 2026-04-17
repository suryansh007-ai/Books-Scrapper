import requests
url = "https://books.toscrape.com/"
response = requests.get(url)
response.encoding = 'utf-8'
print(response.status_code)
html = response.text


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "lxml")
print(soup.title.text)  


books = soup.find_all("article", class_="product_pod")
book = books[0]
title = book.find("h3").find("a")["title"]
price = book.find("p", class_="price_color").text
availability = book.find("p", class_="instock availability").text.strip()
rating = book.find("p", class_="star-rating")["class"][1]
data = {
    "title": title,
    "price": price,
    "availability": availability,
    "rating": rating
}
print(data)


all_books=[]
for i in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    for book in books:
       title = book.find("h3").find("a")["title"]
       price = book.find("p", class_="price_color").text
       availability = book.find("p", class_="instock availability").text.strip()
       rating = book.find("p", class_="star-rating")["class"][1]
       all_books.append({
         "title": title,
    "price": price,
    "availability": availability,
    "rating": rating
  })
print(all_books)
print("Total Number of books:",len(all_books))


import json
with open("books.json","w",encoding="utf-8")as f:
    json.dump(all_data, f, indent=4)