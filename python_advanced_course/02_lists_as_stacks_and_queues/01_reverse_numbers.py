line = input().split(" ")
result = []
for _ in range(len(line)):
    result.append(line.pop())
print(" ".join(result))
