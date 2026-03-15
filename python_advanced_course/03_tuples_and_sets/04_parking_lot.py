num_of_commands = int(input())
parking = set()

for _ in range(num_of_commands):
    command = input()
    direction, plate = command.split(", ")

    if direction == "IN":
        parking.add(plate)
    elif direction == "OUT":
        if plate in parking:
            parking.remove(plate)

if parking:
    for car in parking:
        print(car)
else:
    print("Parking Lot is Empty")
