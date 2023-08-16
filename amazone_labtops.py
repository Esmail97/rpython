import requests 
from bs4 import BeautifulSoup
import csv

url = 'https://www.amazon.com/s?k=laptops'

# Get page content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Extract product information 
products = []
results = soup.find_all('div', {'data-component-type': 's-search-result'})

for item in results:
    title = item.find('h2').text.strip()
    url = "https://www.amazon.com" + item.find('a', {'class': 'a-link-normal'})['href']
    try:
        rating = item.find('i', {'class': 'a-icon'}).text.strip()
    except AttributeError:
        rating = None
    try:
        reviews = item.find('span', {'class': 'a-size-base'}).text
    except:
        reviews = None
        
    product = {
        'title': title,
        'rating': rating,
        'reviews': reviews,
        'url': url
    }
    
    products.append(product)
    
# Save data to CSV file
with open('products.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=products[0].keys())
    writer.writeheader()
    writer.writerows(products)
