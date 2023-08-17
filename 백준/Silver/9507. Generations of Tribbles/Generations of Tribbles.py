from sys import stdin

dp = [1, 1, 2, 4]
for i in range(3, 70):
    dp.append(dp[-1] + dp[-2] + dp[-3] + dp[-4])

for _ in range(int(stdin.readline())):
    print(dp[int(stdin.readline())])
