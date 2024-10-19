import requests, simplejson

def get_data(): 
    while True:
        base = input('Choose currency base: ').lower()
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base}.json'

        response = requests.get(url)
        if response.status_code == 200:
            break
        else:
            print('Currency not found!')
            continue

    data = response.json()
    data = data[base]
    
    return base, data

base, data = get_data()
while True:
    res_cur = input('Choose currency to convert: ').lower()
    try:
        data[res_cur]
    except KeyError: 
        print('Currency not found!')
        continue
    value = input('Value to convert: ')
    try: 
        value = int(value)
        break
    except ValueError:
        print('Value must be an integer!')
        continue

result = data[res_cur] * value
print(f'{value}x {base} = {result} {res_cur}')
