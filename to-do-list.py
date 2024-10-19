import os

def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
  menu = ['1) Add task', '2) Remove from list', '0) Exit']  
  print('_____________________')
  for i in menu:
    print(i) 
  print('---------------------')

def show_tasks():
  clear()
  print("Current tasks: ")
  for i in range(0,len(to_do)):
    print(f'{i}) {to_do[i]}')

def add_task():
  clear()
  show_tasks()
  task = input('--> ')
  to_do.append(task)
  show_tasks() 

def remove_task():
  clear()
  show_tasks()
  while True:
    done = input('--> ')
    try:
      done = int(done)
      try:
        to_do.pop(done)
        break
      except IndexError:
        print('List index out of range')
        continue
    except ValueError:
      print('Index only!')
      continue

  show_tasks()

to_do = []
while True:
  show_tasks()
  show_menu()

  operation = input('Choose operation: ')

  match operation:
    case '1':
      add_task()
    case '2':
      remove_task()
    case '0':
      quit()
