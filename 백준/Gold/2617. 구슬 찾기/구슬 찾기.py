from sys import stdin

n, m = map(int, stdin.readline().split())
wei = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    wei[a][b] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if wei[i][k] and wei[k][j]:
                wei[i][j] = 1

ans = 0

for x in range(1, n + 1):
    l, r = 0, 0

    for y in range(1, n + 1):
        if wei[x][y]:
            l += 1

        if wei[y][x]:
            r += 1

    if l > n // 2 or r > n // 2:
        ans += 1

print(ans)