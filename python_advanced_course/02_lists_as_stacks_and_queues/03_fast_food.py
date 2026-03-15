from collections import deque

food_quantity = int(input())
orders_queue = deque(int(x) for x in input().split())
print(max(orders_queue))

while orders_queue and orders_queue[0] <= food_quantity:
    food_quantity -= orders_queue.popleft()

if orders_queue:
    print("Orders left:", *orders_queue)

else:
    print("Orders complete")
