size = int(input())
matrix = []
my_position = []

health = 100
stars = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

for row in range(size):
    r = list(input())
    matrix.append(r)
    for col, el in enumerate(r):
        if el == "P":
            my_position = [row, col]
        elif el == "*":
            stars += 1

freezer = 0
while True:
    command = input()
    if not stars:
        break
    if health <= 0:
        break
    if command == "end":
        break

    matrix[my_position[0]][my_position[1]] = "-"
    my_position[0] += directions[command][0]
    my_position[1] += directions[command][1]
    row = my_position[0]
    col = my_position[1]

    if row < 0:
        row = len(matrix) - 1
    elif row >= len(matrix):
        row = 0
    if col < 0:
        col = len(matrix) - 1
    elif col >= len(matrix):
        col = 0

    my_position[0] = row
    my_position[1] = col

    if matrix[row][col] == "-":
        continue
    elif matrix[row][col] == "*":
        stars -= 1
        matrix[row][col] = "-"
        continue
    elif matrix[row][col] == "G":
        if freezer == 1:
            freezer = float("-inf")
            matrix[row][col] = "-"
            continue
        health -= 50
        matrix[row][col] = "-"
        continue
    elif matrix[row][col] == "F":
        freezer += 1
        matrix[row][col] = "-"
        continue

matrix[my_position[0]][my_position[1]] = "P"

if health <= 0:
    print(f"Game over! Pacman last coordinates [{my_position[0]},{my_position[1]}]")

if not stars:
    print("Pacman wins! All the stars are collected.")

if health > 0 and stars:
    print("Pacman failed to collect all the stars.")

print(f"Health: {health}")

if stars:
    print(f"Uncollected stars: {stars}")

for row in matrix:
    print("".join(row))
