def boarding_passengers(*args):
    capacity = args[0]
    passengers_list = list(args[1:])
    passengers = {}
    boarded = {}

    all_passengers = 0
    boarded_passengers = 0
    for key in passengers_list:
        all_passengers += key[0]

    for number, group in passengers_list:
        if capacity == 0:
            break
        if number <= capacity:
            if group in boarded:
                boarded[group] += number
            else:
                boarded[group] = number
            capacity -= number
            boarded_passengers += number
        else:
            continue
        if capacity == 0:
            break

    sorted_boarding = sorted(boarded.items(), key=lambda x: (-x[1], x[0]))
    result = ""

    result_lines = [f"## {k}: {v} guests" for k, v in sorted_boarding]
    result = "\n".join(result_lines)

    if all_passengers == boarded_passengers:
        result += "\nAll passengers are successfully boarded!"

    elif not capacity and boarded_passengers < all_passengers:
        result += "\nBoarding unsuccessful. Cruise ship at full capacity."

    elif capacity and boarded_passengers < all_passengers:
        result += f"\nPartial boarding completed. Available capacity: {capacity}."

    return f"Boarding details by benefit plan:\n{result}"


print(boarding_passengers(150, (35, 'Diamond'), (55, 'Platinum'), (35, 'Gold'), (25, 'First Cruiser')))
print(boarding_passengers(100, (20, 'Diamond'), (15, 'Platinum'), (25, 'Gold'), (25, 'First Cruiser'), (15, 'Diamond'),
                          (10, 'Gold')))
print(boarding_passengers(120, (30, 'Gold'), (20, 'Platinum'), (30, 'Diamond'), (10, 'First Cruiser'), (31, 'Platinum'),
                          (20, 'Diamond')))
