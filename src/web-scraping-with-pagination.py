import requests
from bs4 import BeautifulSoup

url = input("URL: ")
page = int(input('Number of pages: '))

for i in range(1, page):
    response = requests.get(url+f'?page={i}', timeout=10)
    soup = BeautifulSoup(response.content, 'html.parser')
    print(soup)

