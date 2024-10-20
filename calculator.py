# Define available operations
operations = {
    '1': ('sum', lambda x, y: x + y),
    '2': ('difference', lambda x, y: x - y),
    '3': ('multiply', lambda x, y: x * y),
    '4': ('division', lambda x, y: x / y)
}

# Display the available operations
print('_____________________')
for key, (name, _) in operations.items():
    print(f"{key}) {name}")
print('_____________________\n')

# Get user input
operation = input('Choose operation (1-4): ')
num1 = int(input('Choose num1: '))
num2 = int(input('Choose num2: '))

# Execute the chosen operation
if operation in operations:
    _, func = operations[operation]
    result = func(num1, num2)
    print('Result:', result)
else:
    print('Operation not found!')
