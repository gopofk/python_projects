r, c = map(int, input().split())
matrix = []
bunnies = set()

for row in range(r):
    matrix.append(list(input()))
    for col in range(c):
        if matrix[row][col] == "P":
            p_row, p_col = row, col
        elif matrix[row][col] == "B":
            bunnies.add((row, col))

commands = input()

moves = {
    "U": lambda r, c: (r - 1, c),
    "D": lambda r, c: (r + 1, c),
    "L": lambda r, c: (r, c - 1),
    "R": lambda r, c: (r, c + 1)
}


def spread_bunnies(mat, bunny_set):
    new_bunnies = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for br, bc in bunny_set:
        for dr, dc in directions:
            nr, nc = br + dr, bc + dc
            if 0 <= nr < r and 0 <= nc < c:
                mat[nr][nc] = "B"
                new_bunnies.add((nr, nc))

    return mat, bunny_set | new_bunnies


won = False

for command in commands:
    next_r, next_c = moves[command](p_row, p_col)

    matrix[p_row][p_col] = "."

    # WIN
    if next_r < 0 or next_r >= r or next_c < 0 or next_c >= c:
        won = True
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        break

    p_row, p_col = next_r, next_c

    # DEAD from bunny
    if matrix[p_row][p_col] == "B":
        matrix, bunnies = spread_bunnies(matrix, bunnies)
        break

    matrix[p_row][p_col] = "P"
    matrix, bunnies = spread_bunnies(matrix, bunnies)

    if matrix[p_row][p_col] == "B":
        break

for row in matrix:
    print("".join(row))

if won:
    print(f"won: {p_row} {p_col}")
else:
    print(f"dead: {p_row} {p_col}")
