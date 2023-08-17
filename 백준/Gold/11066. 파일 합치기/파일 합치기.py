from sys import stdin


def solve():
    n = int(stdin.readline().strip())
    arr = list(map(int, stdin.readline().split()))

    dp = [[0] * n for _ in range(n)]

    for j in range(1, n):
        for i in range(j - 1, -1, -1):
            small = 1e9
            for k in range(j - i):
                small = min(small, dp[i][i + k] + dp[i + k + 1][j])
            dp[i][j] = small + sum(arr[i:j + 1])
    print(dp[0][n - 1])


for _ in range(int(stdin.readline().strip())):
    solve()