import requests
from bs4 import BeautifulSoup

def web_scrape():
    print("Welcome to the Web Scraping Script!")
    url = input("Enter the URL to scrape: ")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Example: Extract and print all paragraph texts
    for paragraph in soup.find_all('p'):
        print(paragraph.text)

if __name__ == "__main__":
    web_scrape()
