from sys import stdin

n, m = map(int, stdin.readline().split())
l = [x for x in range(1, n + 1)]
for _ in range(m):
    a, b = map(int, stdin.readline().split())
    temp = l[a-1:b]
    temp.reverse()
    idx = 0
    for x in range(a - 1, b):
        l[x] = temp[idx]
        idx += 1

print(*l)