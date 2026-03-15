from collections import deque
from math import floor

tokens = input().split()
queue = deque()

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: floor(a / b),
}

for token in tokens:
    if token in operations:
        result = queue.popleft()
        while queue:
            result = operations[token](result, queue.popleft())
        queue.append(result)
    else:
        queue.append(int(token))

print(queue.pop())
