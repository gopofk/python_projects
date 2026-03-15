matrix = []

for _ in range(int(input())):
    matrix.append(list(input()))

searched_char = input()
is_found = False
row_and_index = ()

for row in range(len(matrix)):
    if is_found:
        break
    for i in range(len(matrix[0])):
        if matrix[row][i] == searched_char:
            is_found = True
            row_and_index = row, i
            break

if is_found:
    print(row_and_index)
else:
    print(f"{searched_char} does not occur in the matrix")
