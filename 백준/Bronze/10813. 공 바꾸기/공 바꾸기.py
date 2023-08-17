from sys import stdin

n, m = map(int, stdin.readline().split())
l = [x for x in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    l[a-1], l[b-1] = l[b-1], l[a-1]

print(*l)