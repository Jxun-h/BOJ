from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)

n, m = map(int, stdin.readline().split())
arr = sorted(list(map(int, stdin.readline().split())))
ans, d = set(), {}
for i in set(arr):
    d[i] = arr.count(i)


def f(res, cnt):
    if cnt == m:
        ans.add(tuple(res))
        return

    for i in arr:
        if cnt > 0:
            if res[-1] <= i:
                if d[i] > 0:
                    d[i] -= 1
                    f(res + [i], cnt + 1)
                    d[i] += 1
        else:
            if d[i] > 0:
                d[i] -= 1
                f(res + [i], cnt + 1)
                d[i] += 1


f([], 0)
for i in sorted(list(ans)):
    print(*i)