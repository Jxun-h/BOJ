from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    coin = list(map(int, stdin.readline().split()))
    money = int(stdin.readline())
    dp = [0 for _ in range(money + 1)]
    dp[0] = 1

    for i in coin:
        for j in range(money + 1):
            if j >= i:
                dp[j] += dp[j - i]

    print(dp[money])

