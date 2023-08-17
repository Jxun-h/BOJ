from sys import stdin
from bisect import bisect_right, bisect_left

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
arr.sort()
x = int(stdin.readline())

cnt = 0

for i in range(n):
    l, r = bisect_left(arr, x - arr[i]), bisect_right(arr, x - arr[i])
    if l < n:
        if arr[i] != arr[l] and l != r:
            cnt += 1

print(cnt//2)
