import sys
import os
import random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

x = random.randint(1, 101)


while True:
    clear()
    print('Welcome to Guessing game!!!')
    print('I will choose numbet between 1-100, and you have to guess it!')
    print('You will have 5 tries, each try you will get a hint.\nGood luck!')
    hint = ''
    tries = 5

    while tries > 0:
        print(f'You have {tries} tries left!')
        print(hint)
        guess = input('Guess the number: ')
        while True:
            try:
                int(guess)
                break
            except ValueError:
                print("Guess isn't number, try again!")
                continue
        if int(guess) > x:
            hint = guess + ' > X'
            continue
        if int(guess) < x:
            hint = guess + ' < X'
        elif int(guess) == x:
            print('You WIN!')
            replay = input('Do you wish you play again?(y/N): ')
            if replay == 'y':
                break
            sys.exit()
        clear()
        tries -= 1
    print('You are out of tries...')
    replay = input('Do you wish you play again?(y/N): ')
    if replay == 'y':
        continue
    sys.exit()
