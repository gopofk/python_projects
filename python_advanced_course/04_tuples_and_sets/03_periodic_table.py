num = int(input())
chemicals_set = set()
for _ in range(num):
    chemical = input().split()
    for chem in chemical:
        chemicals_set.add(chem)

print(*chemicals_set, sep="\n")
