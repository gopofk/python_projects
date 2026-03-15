from collections import deque

r, c = [int(x) for x in input().split()]
the_snake = deque(input())

matrix = []

for row in range(r):
    matrix.append([""] * c)
    for col in range(c):
        if row % 2 == 0:
            matrix[row][col] = the_snake[0]
        else:
            matrix[row][-1 - col] = the_snake[0]
        the_snake.rotate(-1)

for row in matrix:
    print(*row, sep="")
