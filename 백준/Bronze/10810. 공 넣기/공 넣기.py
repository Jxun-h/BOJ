from sys import stdin

n, m = map(int, stdin.readline().split())
l = [0 for _ in range(n)]
for _ in range(1, m + 1):
    a, b, c = map(int, stdin.readline().split())
    for i in range(a-1, b):
        l[i] = c

print(*l)