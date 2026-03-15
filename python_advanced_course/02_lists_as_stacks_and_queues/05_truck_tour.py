from collections import deque

number_of_petrol_pumps = int(input())
pumps = deque()

for _ in range(number_of_petrol_pumps):
    current_fuel, current_distance = input().split()
    pumps.append({"fuel": int(current_fuel), "dist": int(current_distance)})

start_position = 0
stops = 0

while stops < number_of_petrol_pumps:
    fuel = 0
    for i in range(number_of_petrol_pumps):
        fuel += pumps[i]["fuel"]
        distance = pumps[i]["dist"]
        if fuel < distance:
            pumps.rotate(-1)
            start_position += 1
            stops = 0
            break
        fuel -= distance
        stops += 1

print(start_position)
