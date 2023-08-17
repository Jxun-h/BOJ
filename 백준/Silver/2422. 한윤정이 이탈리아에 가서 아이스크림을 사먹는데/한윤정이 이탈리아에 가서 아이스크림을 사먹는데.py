from sys import stdin
from itertools import combinations

n, m = map(int, stdin.readline().split())
ice_cream = set(x for x in range(1, n + 1))
nope = {x: set() for x in range(1, n + 1)}

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    nope[a].add(b)
    nope[b].add(a)


res = 0
for comb in list(set(combinations(ice_cream, 3))):
    if comb[1] not in nope[comb[0]] and comb[2] not in nope[comb[0]] and comb[1] not in nope[comb[2]]:
        res += 1

print(res)