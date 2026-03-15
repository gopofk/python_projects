from collections import deque

robots_input = input().split(";")

hours, minutes, seconds = input().split(":")
current_time = (int(hours) * 3600) + (int(minutes) * 60) + int(seconds)

robots = []
for robot in robots_input:
    robot_name, working_time = robot.split("-")

    current_robot = {
        "robot_name": robot_name,
        "working_time": int(working_time),
        "free_at": current_time % 86400,
    }
    robots.append(current_robot)

line = deque()
while True:
    product = input()
    if product == "End":
        break
    else:
        line.append(product)

while line:
    current_time += 1
    current_time %= 86400
    current_product = line[0]
    for robot in robots:
        if robot["free_at"] <= current_time:
            hours = current_time // 3600
            minutes = (current_time % 3600) // 60
            seconds = current_time % 60

            print(f"{robot['robot_name']} - {current_product} [{hours:02d}:{minutes:02d}:{seconds:02d}]")
            robot["free_at"] = current_time + robot["working_time"]
            line.popleft()
            break

    else:
        current_product = line.popleft()
        line.append(current_product)

# chat GPT version

from collections import deque

# Read robots
robots_input = input().split(";")

# Read start time and convert to seconds
hours, minutes, seconds = input().split(":")
current_time = int(hours) * 3600 + int(minutes) * 60 + int(seconds)

robots = []
for robot in robots_input:
    robot_name, working_time = robot.split("-")
    robots.append({
        "robot_name": robot_name,
        "working_time": int(working_time),
        "free_at": current_time
    })

# Read products
line = deque()
while True:
    product = input()
    if product == "End":
        break
    line.append(product)

# Simulation
while line:
    # 1 second passes
    current_time = (current_time + 1) % 86400

    current_product = line[0]
    product_taken = False

    for robot in robots:
        if robot["free_at"] <= current_time:
            h = current_time // 3600
            m = (current_time % 3600) // 60
            s = current_time % 60

            print(f"{robot['robot_name']} - {current_product} [{h:02d}:{m:02d}:{s:02d}]")

            robot["free_at"] = (current_time + robot["working_time"]) % 86400
            line.popleft()
            product_taken = True
            break

    if not product_taken:
        line.append(line.popleft())
