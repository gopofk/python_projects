file = open("numbers.txt")
result = 0
for num in file:
    result += int(num)

print(result)
