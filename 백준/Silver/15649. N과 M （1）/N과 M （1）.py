from sys import stdin
from itertools import permutations

n, m = map(int, stdin.readline().split())
for per in list(permutations([i for i in range(1, n + 1)], m)):
    print(*per)
