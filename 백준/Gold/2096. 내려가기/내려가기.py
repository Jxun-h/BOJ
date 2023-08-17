from sys import stdin

n = int(stdin.readline())

x_dp = [0] * 3
n_dp = [0] * 3

x_temp = [0] * 3
n_temp = [0] * 3

for i in range(n):
    a, b, c = map(int, stdin.readline().split())
    for j in range(3):
        if j == 0:
            x_temp[j] = a + max(x_dp[j], x_dp[j + 1])
            n_temp[j] = a + min(n_dp[j], n_dp[j + 1])

        elif j == 1:
            x_temp[j] = b + max(x_dp[j - 1], x_dp[j], x_dp[j + 1])
            n_temp[j] = b + min(n_dp[j - 1], n_dp[j], n_dp[j + 1])

        elif j == 2:
            x_temp[j] = c + max(x_dp[j], x_dp[j - 1])
            n_temp[j] = c + min(n_dp[j], n_dp[j - 1])

    for j in range(3):
        x_dp[j] = x_temp[j]
        n_dp[j] = n_temp[j]

print(max(x_dp), min(n_dp))