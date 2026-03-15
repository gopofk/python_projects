from collections import deque

chocolate_stack = list(map(int, input().split(", ")))
milk_queue = deque(map(int, input().split(", ")))

milkshakes = 0

while chocolate_stack and milk_queue and milkshakes < 5:

    # Remove all invalid values BEFORE mixing
    if chocolate_stack[-1] <= 0 or milk_queue[0] <= 0:
        if chocolate_stack[-1] <= 0:
            chocolate_stack.pop()
        if milk_queue[0] <= 0:
            milk_queue.popleft()
        continue

    chocolate = chocolate_stack.pop()
    milk = milk_queue.popleft()

    if chocolate == milk:
        milkshakes += 1
    else:
        milk_queue.append(milk)
        chocolate -= 5
        if chocolate > 0:
            chocolate_stack.append(chocolate)

# Output
if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolate_stack:
    print("Chocolate:", ", ".join(map(str, chocolate_stack)))
else:
    print("Chocolate: empty")

if milk_queue:
    print("Milk:", ", ".join(map(str, milk_queue)))
else:
    print("Milk: empty")
