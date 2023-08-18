from sys import stdin
from itertools import combinations_with_replacement

n = int(stdin.readline())
rome = [1, 5, 10, 50]
visited = [1 for _ in range(1001)]
ans = 0

for comb in list(combinations_with_replacement(rome, n)):
    res = sum(comb)
    if visited[res]:
        visited[res] = 0
        ans += 1

print(ans)