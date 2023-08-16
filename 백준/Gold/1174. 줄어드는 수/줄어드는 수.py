from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 7)
result = set()
arr = []


def solve():
    if len(arr) > 0:
        result.add(int(''.join(map(str, arr))))

    for i in range(0, 10):
        if len(arr) == 0 or arr[-1] > i:
            arr.append(i)
            solve()
            arr.pop()


n = int(stdin.readline())
solve()
result = list(result)
result.sort()

if len(result) < n:
    print(-1)
else:
    print(result[n - 1])