from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_stack = list(map(int, input().split()))
locks_queue = deque(map(int, input().split()))
money = int(input())
shots = 0

while bullets_stack and locks_queue:
    shots += 1
    current_bullet = bullets_stack.pop()
    money -= bullet_price
    current_lock = locks_queue[0]

    if current_lock >= current_bullet:
        locks_queue.popleft()
        print("Bang!")
    else:
        print("Ping!")

    if shots == gun_barrel_size and bullets_stack:
        print("Reloading!")
        shots = 0

if locks_queue:
    print(f"Couldn't get through. Locks left: {len(locks_queue)}")
else:
    print(f"{len(bullets_stack)} bullets left. Earned ${money}")
