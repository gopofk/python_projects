rows = int(input())
chess_board = [list(input()) for row in range(rows)]


def attacks(coordinates, matrix):
    row, col = coordinates[0], coordinates[1]
    available_attacks = 0

    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]

    for dr, dc in moves:
        if 0 <= row + dr < len(matrix) and 0 <= col + dc < len(matrix[0]):
            if matrix[row + dr][col + dc] == "K":
                available_attacks += 1

    return available_attacks


knights_at = set()
for row in range(len(chess_board)):
    for col in range(len(chess_board[0])):
        current_cell = chess_board[row][col]
        if current_cell == "K":
            knights_at.add((row, col))

removed_knights = 0

while True:
    max_attacks = 0
    knight_to_remove = None

    for k in knights_at:
        current_k_attacks = attacks(k, chess_board)

        if current_k_attacks > max_attacks:
            max_attacks = current_k_attacks
            knight_to_remove = k

        if knight_to_remove:
            if current_k_attacks == max_attacks:
                if k[0] < knight_to_remove[0]:
                    knight_to_remove = k
                elif k[0] == knight_to_remove[0] and k[1] < knight_to_remove[1]:
                    knight_to_remove = k

    if max_attacks == 0:
        break

    chess_board[knight_to_remove[0]][knight_to_remove[1]] = "0"
    knights_at.remove(knight_to_remove)
    removed_knights += 1

print(removed_knights)
