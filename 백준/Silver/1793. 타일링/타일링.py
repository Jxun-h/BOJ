from sys import stdin

dp = [0 for _ in range(251)]
dp[0], dp[1] = 1, 1

for i in range(2, 251):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

while 1:
    try:
        print(dp[int(stdin.readline())])

    except:
        break