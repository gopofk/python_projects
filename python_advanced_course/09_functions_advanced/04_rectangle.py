def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    def area(l, w):
        return l * w

    def perimeter(l, w):
        return 2 * (l + w)

    return f"Rectangle area: {area(length, width)}\nRectangle perimeter: {perimeter(length, width)}"


print(rectangle('2', 10))
