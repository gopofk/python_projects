num_of_lines = int(input())
names = []
for _ in range(num_of_lines):
    name = input()
    names.append(name)

unique_names = {name for name in names}

for name in unique_names:
    print(name)
