matrix = []
result = 0

for _ in range(int(input())):
    matrix.append(list(map(int, input().split())))

for i in range(len(matrix[0])):
    result += matrix[i][i]

print(result)
