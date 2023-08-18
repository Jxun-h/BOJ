from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort()
ans = set()


def f(res, cnt):
    if cnt == m:
        ans.add(tuple(res))
        return
    for i in arr:
        f(res + [i], cnt + 1)


f([],0)

for i in sorted(list(ans)):
    print(*i)
