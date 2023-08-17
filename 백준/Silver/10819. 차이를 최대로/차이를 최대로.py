from sys import stdin
from itertools import permutations

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
res = -int(1e9)

for arr2 in permutations(arr, n):
    v = 0
    for i in range(n-1):
        v += abs(arr2[i] - arr2[i + 1])

    res = max(res, v)

print(res)