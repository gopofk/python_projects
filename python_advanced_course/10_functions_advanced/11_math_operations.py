def math_operations(*args, **kwargs):
    keys = ["a", "s", "d", "m"]
    operations = {
        "a": lambda a, b: a + b,
        "s": lambda a, b: a - b,
        "d": lambda a, b: a / b,
        "m": lambda a, b: a * b
    }

    for i, num in enumerate(args):
        op = i % 4
        if keys[op] == "d":
            if num == 0:
                continue

        kwargs[keys[op]] = operations[keys[op]](kwargs[keys[op]], num)

    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    result = []
    for key, value in sorted_items:
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
