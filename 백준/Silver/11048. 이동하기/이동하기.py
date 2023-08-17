from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
candy = [[0] * m for _ in range(n)]
res = 0

for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

candy[0][0] = arr[0][0]

for i in range(1, m):
    candy[0][i] = arr[0][i] + candy[0][i - 1]

for i in range(1, n):
    candy[i][0] = arr[i][0] + candy[i - 1][0]


for i in range(1, n):
    for j in range(1, m):
        candy[i][j] = max(candy[i - 1][j], candy[i][j - 1], candy[i - 1][j - 1]) + arr[i][j]

print(candy[n - 1][m - 1])