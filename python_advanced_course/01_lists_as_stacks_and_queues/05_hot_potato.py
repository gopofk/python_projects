from collections import deque

kids_names = input().split(" ")
kids = deque(kids_names)
nth_toss = int(input())

while len(kids) > 1:
    kids.rotate(-nth_toss + 1)
    print(f"Removed {kids.popleft()}")

print(f"Last is {kids.pop()}")
