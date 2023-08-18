from sys import stdin

a, b, c = list(map(int, stdin.readline().rstrip("\n").split()))
x1, x2, y1, y2 = list(map(int, stdin.readline().rstrip("\n").split()))
X = [x1, x2]
Y = [y1, y2]


def solve(sign):
    for x in X:
        for y in Y:
            r = a * x + b * y + c
            if r == 0:
                print("Lucky")
                return
            if sign == 0 and r > 0:
                sign = 1
            elif sign == 0 and r < 0:
                sign = -1
            if r * sign < 0:
                print("Poor")
                return
    print("Lucky")


solve(0)
