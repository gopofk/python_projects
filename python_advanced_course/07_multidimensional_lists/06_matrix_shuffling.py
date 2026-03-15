rows, cols = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]

while True:
    command = input()

    if command == "END":
        break

    parts = command.split()

    if parts[0] != "swap" or len(parts) != 5:
        print("Invalid input!")
        continue

    _, r1, c1, r2, c2 = parts

    if not (r1.isdigit() and c1.isdigit() and r2.isdigit() and c2.isdigit()):
        print("Invalid input!")
        continue

    r1, c1, r2, c2 = map(int, (r1, c1, r2, c2))

    if not (0 <= r1 < rows and 0 <= c1 < cols and
            0 <= r2 < rows and 0 <= c2 < cols):
        print("Invalid input!")
        continue

    # swap
    matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]

    for row in matrix:
        print(*row)
