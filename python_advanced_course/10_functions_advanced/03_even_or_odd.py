def even_odd(*args):
    command = args[-1]
    result = None

    if command == "even":
        result = list(filter(lambda x: x % 2 == 0, args[:-1]))
    else:
        result = list(filter(lambda x: x % 2 != 0, args[:-1]))

    return result


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
