import requests 

def get_data(): 
    while True:
        base_cur = input('Choose currency base: ').lower()
        url = f'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/{base}.json'

        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            break
        print('Currency not found!')
        continue

    data_cur = response.json()
    data_cur = data_cur[base]
    return base_cur, data_cur

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
