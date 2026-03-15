from collections import deque

working_bees_queue = deque(list(map(int, input().split())))
nectar_stack = list(map(int, input().split()))
symbols_queue = deque(list(map(str, input().split())))
total_honey = 0

symbols_functions = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}

while working_bees_queue and nectar_stack:
    if working_bees_queue[0] <= nectar_stack[-1]:
        current_bee = working_bees_queue.popleft()
        current_nectar = nectar_stack.pop()
        current_symbol = symbols_queue.popleft()

        if current_symbol == "/":
            if current_nectar == 0:
                continue
        total_honey += abs(symbols_functions[current_symbol](current_bee, current_nectar))
    else:
        nectar_stack.pop()

print(f"Total honey made: {total_honey}")
if working_bees_queue:
    print(f"Bees left: {', '.join(map(str, working_bees_queue))}")
if nectar_stack:
    print(f"Nectar left: {', '.join(map(str, nectar_stack))}")
