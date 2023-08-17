from sys import stdin, setrecursionlimit

setrecursionlimit(10 ** 6)

n = int(stdin.readline())


def solve(N, start, mid, end):
    if N == 1:
        print(start, end)
        return

    solve(N - 1, start, end, mid)
    print(start, end)
    solve(N - 1, mid, start, end)


temp = 0
for i in range(n):
    temp *= 2
    temp += 1

print(temp)

if n < 21:
    solve(n, 1, 2, 3)
