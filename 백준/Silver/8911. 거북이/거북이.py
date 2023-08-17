from sys import stdin

for _ in range(int(stdin.readline())):
    x, y, direction = 0, 0, 0
    visited = set()
    for command in list(stdin.readline().rstrip()):
        if command == 'F':
            if direction == 0:
                y += 1

            elif direction == 1:
                x += 1

            elif direction == 2:
                y -= 1

            else:
                x -= 1

        elif command == 'B':
            if direction == 0:
                y -= 1

            elif direction == 1:
                x -= 1

            elif direction == 2:
                y += 1

            else:
                x += 1

        elif command == 'L':
            if direction == 0:
                direction = 3
            else:
                direction -= 1

        elif command == 'R':
            direction += 1
            direction %= 4

        visited.add((x, y))

    max_x, min_x = 0, 0
    max_y, min_y = 0, 0

    for x, y in visited:
        max_x, max_y = max(max_x, x), max(max_y, y)
        min_x, min_y = min(min_x, x), min(min_y, y)

    height = abs(max_y) + abs(min_y)
    width = abs(max_x) + abs(min_x)

    print(height * width)