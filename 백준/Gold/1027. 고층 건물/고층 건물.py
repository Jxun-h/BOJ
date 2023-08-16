from sys import stdin


def get_slope(a, b, c, d):
    return (d - b) / (c - a)


answer = 0
n = int(stdin.readline())
buliding = list(map(int, stdin.readline().split()))

for i, y1 in enumerate(buliding):
    x1 = i + 1
    current, visible_r = None, 0

    for j in range(i + 1, n):
        if j == n:
            break
        x2 = j + 1
        y2 = buliding[j]
        slope = get_slope(x1, y1, x2, y2)

        if current is None or current < slope:
            current = slope
            visible_r += 1

    current, visible_l = None, 0
    for j in range(i - 1, -1, -1):
        if j == -1:
            break
        x2 = j + 1
        y2 = buliding[j]
        slope = get_slope(x1, y1, x2, y2)

        if current is None or current > slope:
            current = slope
            visible_l += 1

    answer = max(answer, visible_l + visible_r)

print(answer)