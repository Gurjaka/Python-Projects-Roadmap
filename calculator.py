items = ['1) sum', '2) difference', '3) multiply', '4) division']
print('_____________________')
for i in items:
    print(i)
print('_____________________\n')

operation = input('Choose operation: ')
num1,num2 = input('Choose num1: '),input('Choose num2: ')
num1,num2 = int(num1),int(num2)

if '1' or 'sum':
    print('Result:', num1 + num2)
elif '2' or 'difference':
    print('Result:', num1 - num2)
elif '3' or 'multiply':
    print('Result:', num1 * num2)
elif '4' or 'division':
    print('Result:', num1 / num2)
else:
    print('Operation not found!')
