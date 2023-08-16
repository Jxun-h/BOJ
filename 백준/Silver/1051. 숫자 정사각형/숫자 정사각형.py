from sys import stdin

n, m = map(int, stdin.readline().split())

arr = [[0] * 51 for _ in range(51)]

for i in range(n):
    data = list(map(int, list(stdin.readline().rstrip())))
    for j in range(len(data)):
        arr[i][j] = data[j]


visited = []
ans = 0

for x in range(n):
    for y in range(m):
        for k in range(51):
            if x + k >= n or k + y >= m:
                break

            if arr[x][y] != arr[x][k + y] or arr[x][y] != arr[x + k][y] or arr[x][y] != arr[x + k][y + k]:
                continue

            ans = max(ans, (k + 1) * (k + 1))

print(ans)