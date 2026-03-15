rows = int(input())
matrix = []

[matrix.append(list(map(int, input().split()))) for _ in range(rows)]

while True:
    commands = input()
    if commands == "END":
        break
    action = commands.split()
    row, col, value = int(action[1]), int(action[2]), int(action[3])

    if row not in range(0, len(matrix)) or col not in range(0, len(matrix)):
        print("Invalid coordinates")
        continue

    if action[0] == "Add":
        matrix[row][col] += value
    elif action[0] == "Subtract":
        matrix[row][col] -= value

[print(*row, sep=" ") for row in matrix]
