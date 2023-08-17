from sys import stdin
from itertools import permutations

n = int(stdin.readline())
for comb in sorted(list(permutations(range(1, n + 1), n))):
    print(*comb)