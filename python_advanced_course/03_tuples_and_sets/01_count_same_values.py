numbers = tuple([float(el) for el in input().split()])
printed = []
for num in numbers:
    if num not in printed:
        print(f"{num} - {numbers.count(num)} times")
        printed.append(num)
