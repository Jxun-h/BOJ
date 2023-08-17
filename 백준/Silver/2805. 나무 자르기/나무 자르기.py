from sys import stdin

n, m = map(int, stdin.readline().split())
forest = list(map(int, stdin.readline().split()))

start, end = 1, max(forest)

while start <= end:
    mid = (start + end) // 2

    res = 0
    for i in forest:
        if i > mid:
            res += i - mid

    if res >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)