rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

matching_square_matrices = 0

for row in range(len(matrix) - 1):
    for column in range(len(matrix[0]) - 1):
        one = matrix[row][column]
        two = matrix[row][column + 1]
        three = matrix[row + 1][column]
        four = matrix[row + 1][column + 1]

        if one == two and two == three and three == four:
            matching_square_matrices += 1

print(matching_square_matrices)
