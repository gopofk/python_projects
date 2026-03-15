num_or_rows = int(input())
field_matrix = []
my_bee = []
energy = 15
nectar = 0

for row in range(num_or_rows):
    field_matrix.append(list(input()))
    for col, el in enumerate(field_matrix[row]):
        if el == "B":
            my_bee = [row, col]
            field_matrix[row][col] = "-"
        elif el.isdigit():
            pass

        elif el == "H":
            pass

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, +1)
}

restored_energy = 0

while energy:
    direction = input()
    possible_move = [my_bee[0] + directions[direction][0], my_bee[1] + directions[direction][1]]
    energy -= 1

    if possible_move[0] >= len(field_matrix):
        possible_move[0] = 0
    elif possible_move[0] < 0:
        possible_move[0] = len(field_matrix) - 1
    elif possible_move[1] >= len(field_matrix):
        possible_move[1] = 0
    elif possible_move[1] < 0:
        possible_move[1] = len(field_matrix) - 1
    my_bee = possible_move

    if field_matrix[my_bee[0]][my_bee[1]].isdigit():
        nectar += int(field_matrix[my_bee[0]][my_bee[1]])
        field_matrix[my_bee[0]][my_bee[1]] = "-"

    elif field_matrix[my_bee[0]][my_bee[1]] == "H":
        if nectar >= 30:
            print(f"Great job, Beesy! The hive is full. Energy left: {energy}")
        else:
            print("Beesy did not manage to collect enough nectar.")
        break

    if energy == 0:
        if not restored_energy:
            if nectar > 30:
                energy = nectar - 30
                nectar = 30
                restored_energy += 1
    if energy == 0:
        print("This is the end! Beesy ran out of energy.")

field_matrix[my_bee[0]][my_bee[1]] = "B"
for row in field_matrix:
    print(*row, sep="")
