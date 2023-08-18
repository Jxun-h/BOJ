from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
n, m = map(int, stdin.readline().split())


def f(arr, cnt):
    if cnt == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if m > 1 and len(arr) > 0:
            if arr[-1] <= i:
                f(arr + [i], cnt + 1)
        else:
            f(arr + [i], cnt + 1)


f([], 0)