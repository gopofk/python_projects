from collections import deque

input_str_queue = deque(input().split())

main_colors = ["red", "yellow", "blue"]
secondary_colors = ["orange", "purple", "green"]

colors_created = []

color_creation = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]
}

while input_str_queue:

    if len(input_str_queue) == 1:
        current_color = input_str_queue.pop()
        if current_color in main_colors or current_color in secondary_colors:
            colors_created.append(current_color)
        continue

    first_sub = input_str_queue[0]
    second_sub = input_str_queue[-1]

    possible_colors = [first_sub + second_sub, second_sub + first_sub]

    found_color = None
    for color in possible_colors:
        if color in main_colors or color in secondary_colors:
            found_color = color
            break

    if found_color:
        colors_created.append(found_color)
        input_str_queue.popleft()
        input_str_queue.pop()
    else:
        first_sub = input_str_queue.popleft()[:-1]
        second_sub = input_str_queue.pop()[:-1]

        index = len(input_str_queue) // 2

        if first_sub:
            input_str_queue.insert(index, first_sub)
            index += 1

        if second_sub:
            input_str_queue.insert(index, second_sub)

final_colors = []

for color in colors_created:
    if color in main_colors:
        final_colors.append(color)
    else:
        needed = color_creation[color]
        if all(c in colors_created for c in needed):
            final_colors.append(color)

print(final_colors)
