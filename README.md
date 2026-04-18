# Books Scraper with Image Dataset

This project scrapes book data and images from http://books.toscrape.com using Python.

## Features
- Extracts book title, price, availability, and rating
- Handles pagination across all pages
- Downloads and stores book images in a separate folder
- Assigns a unique ID to each book
- Links metadata with corresponding image files
- Exports structured data to JSON format

## Tech Stack
- Python
- Requests
- BeautifulSoup

## Installation
pip install -r requirements.txt

## Usage
python scraper.py

## Output
- `books.json` → contains structured metadata for all books
- `images/` → contains downloaded images named using unique book IDs

## Data Format
Each book entry in JSON:

{
  "id": "book_1",
  "title": "...",
  "price": 51.77,
  "availability": "In stock",
  "rating": "Three",
  "image_path": "images/book_1.jpg"
}
