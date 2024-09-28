import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'http://example.com'

# Make a request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Print the parsed content
print(soup.prettify())