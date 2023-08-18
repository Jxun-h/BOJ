from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()


def f(res, cnt):
    if cnt == m:
        print(*res)
        return

    for i in arr:
        if i not in res:
            f(res + [i], cnt + 1)


f([], 0)
