n = int(input())
matrix = [[int(x) for x in input().split(", ")] for _ in range(n)]

primary_list = [matrix[i][i] for i in range(n)]
secondary_list = [matrix[i][-1 - i] for i in range(n)]

print(f"Primary diagonal: {', '.join(str(x) for x in primary_list)}. Sum: {sum(primary_list)}")
print(f"Secondary diagonal: {', '.join(str(x) for x in secondary_list)}. Sum: {sum(secondary_list)}")
