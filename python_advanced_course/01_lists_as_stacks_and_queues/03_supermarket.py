from collections import deque

queue = deque()
while True:
    client = input()
    if client == "End":
        break
    if client == "Paid":
        for _ in range(len(queue)):
            print(queue.popleft())
        continue
    queue.append(client)
print(f"{len(queue)} people remaining.")
