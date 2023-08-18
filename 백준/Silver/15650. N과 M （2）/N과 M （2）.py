from sys import stdin
from itertools import combinations
n, m = map(int, stdin.readline().split())
ans = []
for comb in set(combinations(range(1, n + 1), m)):
    ans.append(comb)
ans.sort()
for i in ans:
    print(*i)