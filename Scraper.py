from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import pandas as pd

# Correct path with raw string or double backslashes
service = Service(r"C:\Users\theon\test\chromedriver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

products = []  # List to store name of the product
prices = []    # List to store price of the product
ratings = []   # List to store rating of the product
driver.get("https://www.flipkart.com/laptops/a~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&amp;amp;amp;amp;amp;amp;amp;amp;amp;uniq=")

content = driver.page_source
# Pass 'html.parser' to BeautifulSoup to remove the warning
soup = BeautifulSoup(content, 'html.parser')

for a in soup.findAll('div', attrs={'class': 'cPHDOP col-12-12'}):
    name = a.find('div', attrs={'class': 'KzDlHZ'})
    price = a.find('div', attrs={'class': 'Nx9bqj _4b5DiR'})
    rating = a.find('div', attrs={'class': 'XQDdHH'})

    if name and price and rating:  # Check if the elements are found
        products.append(name.text)
        prices.append(price.text)
        ratings.append(rating.text)

# Display the collected data in the terminal
for product, price, rating in zip(products, prices, ratings):
    print(f"Product: {product}\nPrice: {price}\nRating: {rating}\n")