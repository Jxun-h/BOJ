from sys import stdin

n = int(stdin.readline())
m = int(stdin.readline())

arr = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    arr[a][b] = True


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if arr[i][k] and arr[k][j]:
                arr[i][j] = True

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if not arr[i][j] and not arr[j][i]:
            cnt += 1
    print(cnt - 1)