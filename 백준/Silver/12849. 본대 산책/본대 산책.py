from sys import stdin

d = int(stdin.readline())
graph = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2, 4, 5], [3, 5, 6], [2, 3, 4, 7], [4, 7], [5, 6]]
dp = [0 for _ in range(8)]
dp[0] = 1

while d:
    d -= 1
    temp = [0 for _ in range(8)]
    for _ in range(8):
        temp[0] = dp[1] + dp[3]
        temp[1] = dp[0] + dp[2] + dp[3]
        temp[2] = dp[1] + dp[3] + dp[4] + dp[5]
        temp[3] = dp[0] + dp[1] + dp[2] + dp[5]
        temp[4] = dp[2] + dp[5] + dp[6]
        temp[5] = dp[2] + dp[3] + dp[4] + dp[7]
        temp[6] = dp[4] + dp[7]
        temp[7] = dp[5] + dp[6]

    for i in range(8):
        dp[i] = temp[i] % 1000000007

print(dp[0])