from sys import stdin

n = int(stdin.readline())
arr = [list(map(int, stdin.readline().split())) for _ in range(n)]
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == j == n - 1:
            print(dp[i][j])
            exit()

        mv = arr[i][j]

        if n > i + mv:
            dp[i + mv][j] += dp[i][j]

        if n > j + mv:
            dp[i][j + mv] += dp[i][j]
