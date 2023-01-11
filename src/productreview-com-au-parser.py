"""
Scrape data from productreview.com.au website
Extract review data and product data
"""
import json

# Download html data using requests
import requests
# Parse html data using BeautifulSoup
from bs4 import BeautifulSoup
# Use regex to extract data
import re

# Define the url to scrape
url = 'https://www.productreview.com.au/listings/aldi#reviews-list'

# Download the html data using requests
html_data = requests.get(url)
html_text = html_data.text
# Parse the html data using BeautifulSoup
soup = BeautifulSoup(html_text, 'html.parser')

# Save html data to a file
with open('productreview-com-au-page-1.html', 'w', encoding='utf-8') as f:
    f.write(html_text)



# # Extract the review data
# review_data = re.search(r"window\.__ssr_data=(.*?);", html_text).group(1)
#
# # Remove first and last characters
# review_data = review_data[1:-1]
# # Unescape the review data
#
# print(review_data)
# review_json = review_data.replace('\\"', '"')
# review_json = json.loads(review_json)

review_divs = soup.find_all("div", id=re.compile('^review'))
...
