import os,random

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

words = ["happy", "hungry", "tired", "water", "book", "big", "hot", "cold", "open", "close"]
warning = ["head", "body", "left hand", "right hand", "left foot", "right foot",]
display = [
"""
     _____
    |     |
    |      
    |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |     |
    |
    |
""",
"""
     _____
    |     |
    |     O
    |     |\\
    |
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |      \\
    |
""",
"""
     _____
    |     |
    |     O
    |    /|\\
    |    / \\
    |
"""]


while True:
    attempts = -1
    word_to_hang = random.choice(words)
    word_output = "_" * len(word_to_hang)
    while attempts < 6:
        clear()
        print("Lets play a hangman game!")
        if attempts >= 0:
            print(f"warning: {warning[attempts]}.")
        print(f"{display[attempts+1]}\n {word_output} {5 - attempts} attempts left.\n")

        if word_output == word_to_hang:
            print("You WIN")
            break

        if attempts == 5:
            print("You lose, you are out of attempts.")
            break

        guess = input("Guess a letter: ")

        if guess not in word_to_hang:
            attempts += 1
            continue

        new_word_output = list(word_output)
        for i in enumerate(word_to_hang):
            if word_to_hang[i] == guess:
                new_word_output[i] = guess
        word_output = "".join(new_word_output) 

    replay = input("Do you wish to play again? (y/N): ")
    if replay == "y":
        continue
    break
