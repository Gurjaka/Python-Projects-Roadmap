import random, time, os

while True:
  os.system('cls' if os.name == 'nt' else 'clear')

  choice_list = ['Rock', 'Paper', 'Scissors']
  print('Lets play a Rock, Paper, Scissors game!!!')
  choice = random.choice(choice_list)

  print('________________')
  for i in range(0,len(choice_list)):
    print(f'{i+1}) {choice_list[i]}')
  print('----------------')
  
  player = input('--> ')
  while True:
    try:
      player = int(player)
      if player > 3 or player < 0:
        raise ValueError
      else:
        break
    except ValueError:
      print('Invalid input! Must be a number 1-3!')
  player = choice_list[player-1]

  print('Rock...')
  time.sleep(1)

  print('Paper...')
  time.sleep(1)

  print('Scissors...')
  time.sleep(1)

  print('SHOOT!!!')
  print(f'You: {player} vs Bot: {choice}')

  if player == 'Rock' and choice == 'Scissors' or player == 'Paper' and choice == 'Rock' or player == 'Scissors' and choice == 'Paper':
    print('You win!')
  elif player == choice:
    print("It's tie!")
  else:
    print('You lose!')
  replay = input('Do you wish to play again?(y/n): ')
  if replay == 'y':
    continue
  else:
    break
