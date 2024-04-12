# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 16:16:39 2024

@author: Debarghya Das
"""

import requests
from bs4 import BeautifulSoup
import csv

def scrape_web(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    
    products = []

    # Extracting product information
    for product in soup.find_all("div", {"class": "s-result-item"}):
        try:
            name = product.find("span", {"class": "a-size-medium"}).text.strip()
            price = product.find("span", {"class": "a-price"}).text.strip()
            rating = product.find("span", {"class": "a-icon-alt"}).text.strip().split()[0]
            products.append({"Name": name, "Price": price, "Rating": rating})
        except:
            pass

    return products

def save_to_csv(products, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['Name', 'Price', 'Rating']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        
        writer.writeheader()
        for product in products:
            writer.writerow(product)

if __name__ == "__main__":
    url = input("Enter Website URL: ")
    products = scrape_web(url)
    save_to_csv(products, "web_scraping.csv")
    print("Scraping and saving completed successfully!")
