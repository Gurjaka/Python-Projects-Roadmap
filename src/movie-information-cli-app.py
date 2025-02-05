import requests
import json

def get_data():
    while True:
        title = input('Title: ')
        url = f'http://www.omdbapi.com/?t={title}&apikey=302a6cbb'

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            break
        print('Film with following title %s not found!', title)
        continue

    info = response.json()
    return info

info = get_data()

for key, value in info.items():
    print(f'{key}: {value}')


