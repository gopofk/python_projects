longest_intersection = set()

for _ in range(int(input())):
    first_range, second_range = input().split("-")
    first_range_start, first_range_end = map(int, first_range.split(","))
    second_range_start, second_range_end = map(int, second_range.split(","))

    first_set = set(range(first_range_start, first_range_end + 1))
    second_set = set(range(second_range_start, second_range_end + 1))
    result_intersection = first_set.intersection(second_set)

    if len(longest_intersection) < len(result_intersection):
        longest_intersection = result_intersection

print(f"Longest intersection is {sorted(longest_intersection)} with length {len(longest_intersection)}")
