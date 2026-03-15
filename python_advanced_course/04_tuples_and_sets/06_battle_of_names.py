rows = 0
even_set = set()
odd_set = set()

for _ in range(int(input())):
    rows += 1
    name = input()
    ascii_sum = sum(ord(c) for c in name)
    result = ascii_sum // rows

    if result % 2 == 0:
        even_set.add(result)
    else:
        odd_set.add(result)

sum_even_set = sum(even_set)
sum_odd_set = sum(odd_set)

if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
