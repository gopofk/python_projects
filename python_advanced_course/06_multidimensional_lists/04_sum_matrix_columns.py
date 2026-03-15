rows, cols = list(map(int, input().split(", ")))
matrix = []
for _ in range(rows):
    matrix.append(list(map(int, input().split())))

for index in range(len(matrix[0])):
    col_sum = 0
    for row in range(len(matrix)):
        col_sum += matrix[row][index]
    print(col_sum)
