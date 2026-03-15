player_1_name = input("Player one name: ")
player_2_name = input("Player two name: ")
player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'?").upper()

while player_1_sign not in ["X" or "O"]:
    print("Please enter either 'X' or 'O'.")
    player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'?").upper()

player_2_sign = "O" if player_1_sign == 'X' else 'X'

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_1_name} starts first!")

turn = 1

while True:
    current_player = player_1_name if turn % 2 != 0 else player_2_name
    current_sign = player_1_sign if turn % 2 != 0 else player_2_sign

    try:
        position = input(f"{current_player} please choose a free position between [1-9]: ")
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9.")
        continue

    turn += 1
