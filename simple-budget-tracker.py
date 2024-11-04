print('Welcome to Simple Budget Tracker CLI!')

INCOME = float(input('Income: '))

expenses = {
    'Utilities': 0,
    'Food': 0,
    'Transport': 0
}

expenses_list = [
    'Exit',
    'Utilities',
    'Food',
    'Transport'
]

while True:
    print('Current expenses:')
    for key, value in expenses.items():
        print(f'{key}: {value}')

    for i, j in enumerate(expenses_list):
        print(f'{i}) {j}')

    expense = input('Choose expense: ')
    if expense.lower() == 'exit' or int(expense) == 0:
        quit()
    else:
        expense = expenses_list[int(expense)]
    value = float(input('Value: '))
    expenses[expense] += value
