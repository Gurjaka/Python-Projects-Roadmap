import requests
from bs4 import BeautifulSoup

url = input("URL: ")
r = requests.get(url, timeout=10)
soup = BeautifulSoup(r.content, 'html.parser')

print(soup)

