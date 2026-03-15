from collections import deque

water_dispenser_quantity = int(input())
people = deque()

while True:
    person = input()
    if person == "Start":
        break
    people.append(person)

while True:
    command = input()
    if command == "End":
        break

    elif command.split(" ")[0] == "refill":
        litters = int(command.split(" ")[1])
        water_dispenser_quantity += litters

    else:
        current_litters = int(command)
        person_name = people.popleft()
        if water_dispenser_quantity >= current_litters:
            print(f"{person_name} got water")
            water_dispenser_quantity -= current_litters
        else:
            print(f"{person_name} must wait")

print(f"{water_dispenser_quantity} liters left")
