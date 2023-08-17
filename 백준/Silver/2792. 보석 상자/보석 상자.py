import math
from sys import stdin

n, m = map(int, stdin.readline().split())
jewel = []

for _ in range(m):
    jewel.append(int(stdin.readline()))


def solve(l, r):
    res = int(1e11)
    while l <= r:
        temp = 0
        mid = (l + r) // 2
        for i in jewel:
            temp += math.ceil(i / mid)

        if temp > n:
            l = mid + 1
        else:
            r = mid - 1
            res = min(res, mid)

    return res


print(solve(1, max(jewel)))