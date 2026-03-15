result = []
for _ in range(int(input())):
    data = list(map(int, input().split(", ")))
    result.extend(data)

print(result)
