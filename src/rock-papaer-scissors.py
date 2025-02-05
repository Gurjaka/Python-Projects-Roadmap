import random
import time
import os

winning_conditions = {
    'Rock': 'Scissors',
    'Paper': 'Rock',
    'Scissors': 'Paper'
}
choice_list = ['Rock', 'Paper', 'Scissors']

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Let\'s play a Rock, Paper, Scissors game!!!')
    choice = random.choice(choice_list)

    print('________________')
    for i, j in enumerate(choice_list):
        print(f'{i + 1}) {j}')
    print('----------------')

    player = input('--> ')
    while True:
        try:
            player = int(player)
            if player > 3 or player < 1:
                raise ValueError
            break
        except ValueError:
            print('Invalid input! Must be a number 1-3!')
            player = input('--> ')

    player = choice_list[player - 1]

    print('Rock...')
    time.sleep(1)

    print('Paper...')
    time.sleep(1)

    print('Scissors...')
    time.sleep(1)

    print('SHOOT!!!')
    print(f'You: {player} vs Bot: {choice}')

    if choice == winning_conditions[player]:
        print('You win!')
    elif player == choice:
        print("It's a tie!")
    else:
        print('You lose!')

    replay = input('Do you wish to play again? (y/n): ')
    if replay.lower() == 'y':
        continue
    break
