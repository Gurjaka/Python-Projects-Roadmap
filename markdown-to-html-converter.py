import markdown

print('Convert from: \n1) String\n2) File')
while True:
    method = input('--> ')
    try:
        method = int(method)
        break
    except ValueError:
        print('Must be integer! Choose using index!')
        continue

if method == 1:
    html = []
    while True:
        text = input('Type your line (QUIT! to exit): ')
        if text == 'QUIT!':
            break
        html.append(markdown.markdown(text))
        continue
    for i in html:
        print(i)

elif method == 2:
    while True:
        name = input('File name in directory (do not enter extension): ')
        try:
            markdown.markdownFromFile(input=f'./{name}.md', output=f'{name}.html')
            print(f'Generated html fild at ./{name}.html')
            break
        except FileNotFoundError:
            print(f"Error: File '{name}' not found. Please check the file name and try again.")
            continue
