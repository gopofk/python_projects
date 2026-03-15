def print_line(size, stars):
    print(" " * (size - stars) + "* " * stars)


def print_upper_part(size):
    for row in range(1, size):
        print_line(size, row)


def print_lower_part(size):
    for row in range(size, 0, -1):
        print_line(size, row)


def print_rhombus(size):
    print_upper_part(size)
    print_lower_part(size)


n = int(input())

print_rhombus(n)
