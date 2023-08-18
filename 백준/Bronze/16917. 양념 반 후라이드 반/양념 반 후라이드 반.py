from sys import stdin

a, b, c, x, y = map(int, stdin.readline().rstrip().split())

if a + b < c * 2:
    print(a * x + b * y)

else:
    t = 2 * c * min(x, y)
    if x >= y:
        d = x - y
        t += min(a * d, 2 * c * d)
    else:
        d = y - x
        t += min(b * d, 2 * c * d)

    print(t)