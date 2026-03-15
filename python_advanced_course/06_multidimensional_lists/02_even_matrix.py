mix_matrix = []
for _ in range(int(input())):
    mix_matrix.append(list(map(int, input().split(", "))))

even_matrix = [[x for x in row if x % 2 == 0] for row in mix_matrix]
print(even_matrix)
