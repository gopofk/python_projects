from collections import deque

packages = [int(x) for x in input().split()]
couriers = deque([int(x) for x in input().split()])

total_weight_delivered = 0

while packages and couriers:
    curr_package = packages[-1]
    curr_courier = couriers[0]
    if curr_courier >= curr_package:
        total_weight_delivered += curr_package
        packages.pop()
        curr_courier -= (2 * curr_package)
        if curr_courier > 0:
            couriers[0] = curr_courier
            couriers.popleft()
            couriers.append(curr_courier)
        else:
            couriers.popleft()
    else:
        packages[-1] = curr_package - curr_courier
        total_weight_delivered += curr_courier
        couriers.popleft()

print(f"Total weight: {total_weight_delivered} kg")
if not packages and not couriers:
    print("Congratulations, all packages were delivered successfully by the couriers today.")

elif packages and not couriers:
    print(
        f"Unfortunately, there are no more available couriers to deliver the following packages: "
        f"{', '.join(map(str, packages))}")

elif couriers and not packages:
    print(
        f"Couriers are still on duty: "
        f"{', '.join(map(str, couriers))} but there are no more packages to deliver.")
