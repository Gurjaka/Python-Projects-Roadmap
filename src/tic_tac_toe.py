import os


def outofbounds(arg: int) -> bool:
    if arg < 1 or arg > 3:  # The valid range should be 1-3
        global notify
        notify = True
        return True
    return False


def win(pos_a: int, pos_b: int) -> bool:
    global player
    symbol = "X" if player == 1 else "O"

    # Row check
    if (
        game_table[pos_b - 1][0]
        == game_table[pos_b - 1][1]
        == game_table[pos_b - 1][2]
        == symbol
    ):
        return True

    # Column check
    if (
        game_table[0][pos_a - 1]
        == game_table[1][pos_a - 1]
        == game_table[2][pos_a - 1]
        == symbol
    ):
        return True

    # Diagonal check
    if game_table[0][0] == game_table[1][1] == game_table[2][2] == symbol:
        return True

    if game_table[0][2] == game_table[1][1] == game_table[2][0] == symbol:
        return True

    return False


notify = False
error = False
taken = False
player = 1
turn = 0
game_table = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

while True:
    os.system("cls" if os.name == "nt" else "clear")

    for row in game_table:
        print(" ".join(row))

    print(f"Player {player}'s turn")

    if notify:
        print("Choose coordinate in range of 1-3")
    elif error:
        print("Error:", error)
    elif taken:
        print("That place is already taken")

    # Reset flags
    notify = False
    error = False
    taken = False

    try:
        x = int(input("X (1-3): "))
        if outofbounds(x):
            continue

        y = int(input("Y (1-3): "))
        if outofbounds(y):
            continue

    except ValueError:
        error = "Invalid input. Enter numbers only!"
        continue

    if game_table[y - 1][x - 1] == "-":
        game_table[y - 1][x - 1] = "X" if player == 1 else "O"
    else:
        taken = True
        continue

    turn += 1

    if turn >= 5 and win(x, y):
        os.system("cls" if os.name == "nt" else "clear")
        for row in game_table:
            print(" ".join(row))
        print(f"Player {player} wins!")
        break

    elif turn == 9:  # All 9 spaces are filled, meaning a tie
        os.system("cls" if os.name == "nt" else "clear")
        for row in game_table:
            print(" ".join(row))
        print("It's a tie!")
        break

    # Switch player
    player = 2 if player == 1 else 1
