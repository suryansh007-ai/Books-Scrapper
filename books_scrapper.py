import requests
from bs4 import BeautifulSoup
import json
import os
from urllib.parse import urljoin

base_url = "http://books.toscrape.com/catalogue/"
os.makedirs("images", exist_ok=True)

all_books = []
book_id = 1  
for i in range(1, 51):
    url = f"{base_url}page-{i}.html"
    
    response = requests.get(url)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.find("h3").find("a")["title"]
        
        price = book.find("p", class_="price_color").text
        price = price.replace("Â£", "").strip()
        
        availability = book.find("p", class_="instock availability").text.strip()
        rating = book.find("p", class_="star-rating")["class"][1]

        
        image_url = book.find("img")["src"]
        full_image_url = urljoin("http://books.toscrape.com/", image_url)
        
        image_filename = f"book_{book_id}.jpg"
        image_path = os.path.join("images", image_filename)
        img_data = requests.get(full_image_url).content
        with open(image_path, "wb") as f:
            f.write(img_data)
        all_books.append({
            "id": f"book_{book_id}",
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "image_path": image_path
        })
        book_id += 1
print("Total books:", len(all_books))
with open("books.json", "w", encoding="utf-8") as f:
    json.dump(all_books, f, indent=4, ensure_ascii=False)
