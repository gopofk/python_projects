def multiply(*args):
    result = 1
    for num in args:
        result *= int(num)
    return result
