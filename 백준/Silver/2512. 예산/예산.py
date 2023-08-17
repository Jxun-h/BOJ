from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
start, end = 0, max(arr)
ans = -int(1e9)

while start <= end:
    mid = (start + end) // 2

    total = 0
    for i in arr:
        total += min(i, mid)

    if total > m:
        end = mid - 1
    else:
        start = mid + 1
        ans = max(ans, mid)

print(ans)