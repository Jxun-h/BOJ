from sys import stdin
from itertools import combinations

n, s = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

cnt = 0

for i in range(1, n+1):
    for j in combinations(arr, i):
        if s == sum(j):
            cnt += 1


print(cnt)