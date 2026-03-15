rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]
sub_matrix = []
biggest_sum = float("-inf")

for row in range(len(matrix) - 2):
    for column in range(len(matrix[0]) - 2):
        current_sum = sum(
            matrix[r][c]
            for r in range(row, row + 3)
            for c in range(column, column + 3)
        )
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            sub_matrix = [
                [matrix[row][column], matrix[row][column + 1], matrix[row][column + 2]],
                [matrix[row + 1][column], matrix[row + 1][column + 1], matrix[row + 1][column + 2]],
                [matrix[row + 2][column], matrix[row + 2][column + 1], matrix[row + 2][column + 2]]
            ]
print(f"Sum = {biggest_sum}")
for row in sub_matrix:
    print(*row)
