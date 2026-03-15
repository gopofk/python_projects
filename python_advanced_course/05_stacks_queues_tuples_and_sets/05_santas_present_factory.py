from collections import deque

materials_stack = list(map(int, input().split()))
magic_queue = deque(list(map(int, input().split())))
crafted_presents: dict[str, int] = {}

presents_dict = {
    "150": "Doll",
    "250": "Wooden train",
    "300": "Teddy bear",
    "400": "Bicycle"
}

while materials_stack and magic_queue:
    curr_mat = materials_stack[-1]
    curr_magic = magic_queue[0]
    total_magic_level = curr_mat * curr_magic

    if curr_mat == 0 or curr_magic == 0:
        if curr_mat == 0:
            materials_stack.pop()
        if curr_magic == 0:
            magic_queue.popleft()
        continue

    if str(total_magic_level) in presents_dict:
        current_crafted_present = presents_dict[str(total_magic_level)]

        if current_crafted_present not in crafted_presents:
            crafted_presents[current_crafted_present] = 1
        else:
            crafted_presents[current_crafted_present] += 1

        materials_stack.pop()
        magic_queue.popleft()
    elif total_magic_level < 0:
        total_magic_level = curr_mat + curr_magic
        materials_stack.pop()
        magic_queue.popleft()
        materials_stack.append(total_magic_level)
    else:
        magic_queue.popleft()
        materials_stack[-1] += 15

if ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or (
        "Teddy bear" in crafted_presents and "Bicycle" in crafted_presents):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials_stack:
    print(f"Materials left: {', '.join(map(str, reversed(materials_stack)))}")
if magic_queue:
    print(f"Magic left: {', '.join(map(str, magic_queue))}")

for present in sorted(crafted_presents):
    print(f"{present}: {crafted_presents[present]}")
