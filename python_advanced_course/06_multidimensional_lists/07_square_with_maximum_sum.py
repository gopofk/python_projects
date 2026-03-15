rows, cols = list(map(int, input().split(", ")))
matrix = []

for _ in range(rows):
    matrix.append(list(map(int, input().split(", "))))

biggest_sum = 0
biggest_matrix = []

for row in range(len(matrix) - 1):
    for index in range(len(matrix[0]) - 1):
        current_sum = matrix[row][index] + matrix[row][index + 1] + matrix[row + 1][index] + matrix[row + 1][index + 1]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            biggest_matrix = [[matrix[row][index], matrix[row][index + 1]],
                              [matrix[row + 1][index], matrix[row + 1][index + 1]]]

print(*biggest_matrix[0], sep=" ")
print(*biggest_matrix[1], sep=" ")
print(biggest_sum)
