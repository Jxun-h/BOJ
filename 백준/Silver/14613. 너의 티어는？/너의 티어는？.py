from sys import stdin

dp = [[0] * 3100 for _ in range(21)]
dp[0][2000] = 1
w, l, d = map(float, stdin.readline().split())

for i in range(1, 21):
    for j in range(1000, 3001):
        if dp[i - 1][j] != 0:
            dp[i][j - 50] += dp[i - 1][j] * l
            dp[i][j + 50] += dp[i - 1][j] * w
            dp[i][j] += dp[i - 1][j] * d

res = [0, 0, 0, 0, 0]

for i in range(1000, 3001):
    if 1000 <= i < 1500:
        res[0] += dp[20][i]

    elif 1500 <= i < 2000:
        res[1] += dp[20][i]

    elif 2000 <= i < 2500:
        res[2] += dp[20][i]

    elif 2500 <= i < 3000:
        res[3] += dp[20][i]

    elif 3000 <= i < 3500:
        res[4] += dp[20][i]


for r in res:
    print('%.8f' % round(r, 8))