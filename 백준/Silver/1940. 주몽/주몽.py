from sys import stdin
from bisect import bisect_left

n = int(stdin.readline())
m = int(stdin.readline())
arr = sorted(list(map(int, stdin.readline().split())))
res = 0
visited = set()
arr.sort()

for i in arr:
    f = bisect_left(arr, m-i)
    if f < n and arr[f] != i:
        temp = arr[f]
        if temp + i == m and (temp, i) not in visited:
            visited.add((temp, i))
            visited.add((i, temp))
            res += 1

print(res)