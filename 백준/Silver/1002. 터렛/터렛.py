from sys import stdin
from math import sqrt

ipt = stdin.readline

num = int(ipt().rstrip())

for step in range(num):
    x1, y1, r1, x2, y2, r2 = ipt().split()
    x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)

    a = (x1-x2) ** 2
    b = (y1-y2) ** 2

    atob = sqrt(a+b)

    if atob == 0 and r1 == r2:
        print(-1)

    elif atob == abs(r1+r2) or atob == abs(r1-r2):
        print(1)

    elif abs(r1-r2) < atob < abs(r1+r2):
        print(2)

    else:
        print(0)