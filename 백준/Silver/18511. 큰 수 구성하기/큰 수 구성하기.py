from sys import stdin, setrecursionlimit
from itertools import product

setrecursionlimit(int(1e9))

n, k = map(str, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)
le = len(n)
res = -int(1e9)


def solve(le):
    global res

    while 1:
        temp = list(product(arr, repeat=le))
        for i in temp:
            t = int(''.join(map(str, i)))
            if int(t) <= int(n):
                res = max(res, t)

        if res == -int(1e9):
            le -= 1
        else:
            return res


solve(le)
print(res)
