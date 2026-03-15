first_sequence = set(map(int, input().split()))
second_sequence = set(map(int, input().split()))

functions = {
    ("Add", "First"): lambda nums: first_sequence.update(nums),
    ("Add", "Second"): lambda nums: second_sequence.update(nums),
    ("Remove", "First"): lambda nums: first_sequence.difference_update(nums),
    ("Remove", "Second"): lambda nums: second_sequence.difference_update(nums),
    ("Check", "Subset"): lambda: print(
        first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))
}

for _ in range(int(input())):
    command = input().split()
    action, target = command[0], command[1]

    if (action, target) in functions:
        if len(command) > 2:
            functions[(action, target)](map(int, command[2:]))
        else:
            functions[(action, target)]()

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")
