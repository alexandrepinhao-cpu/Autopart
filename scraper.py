import requests
from bs4 import BeautifulSoup

class AutoPartScraper:
    def __init__(self, url):
        self.url = url
        self.parts = []

    def fetch_page(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.text
        else:
            return None

    def parse_page(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        # Sample parsing logic; adjust based on actual page structure
        part_elements = soup.find_all('div', class_='part')  # Change this according to the actual class used
        for part in part_elements:
            name = part.find('h2').text  # Change according to the HTML structure
            price = part.find('span', class_='price').text  # Change according to the HTML structure
            self.parts.append({'name': name, 'price': price})

    def scrape(self):
        html = self.fetch_page()
        if html:
            self.parse_page(html)
        else:
            print('Failed to retrieve the page')

# Example usage:
# scraper = AutoPartScraper('https://example.com/autoparts')
# scraper.scrape()
# print(scraper.parts)