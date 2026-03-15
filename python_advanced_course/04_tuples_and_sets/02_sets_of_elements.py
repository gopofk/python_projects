n, m = map(int, input().split())
lines = n + m
n_set = set()
m_set = set()
counter = 1

for _ in range(lines):
    current_el = int(input())
    if counter <= n:
        n_set.add(current_el)
    else:
        m_set.add(current_el)
    counter += 1

for el in n_set.intersection(m_set):
    print(el)
