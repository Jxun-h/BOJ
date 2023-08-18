from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

res = set()
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
ans = set()


def f(res, cnt):
    if cnt == m:
        ans.add(tuple(res))
        return

    for i in arr:
        if cnt > 0:
            if res[-1] <= i:
                f(res + [i], cnt + 1)
        else:
            f(res + [i], cnt + 1)


f([], 0)
for i in sorted(list(ans)):
    print(*i)