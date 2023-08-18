import sys
from sys import stdin

s = stdin.readline().rstrip()
q = int(stdin.readline())
# dp = [0 for _ in range(len(s))]
# calc = False

for _ in range(q):
    data = stdin.readline().split()
    alpha, l, r = data[0], int(data[1]), int(data[2])

    # if calc:
    #     pre = l - 1 if l - 1 > -1 else 0
    #     print(dp[r] - dp[pre])

    # else:
    #     if s[0] == alpha:
    #         dp[0] = 1
    #
    #     for i in range(1, len(s)):
    #         temp = 1 if s[i] == alpha else 0
    #         dp[i] = dp[i - 1] + temp
    #
    #     calc = True
    #     pre = l - 1 if l - 1 > -1 else 0
    #     print(dp[r] - dp[pre])

    print(s[l:r + 1].count(alpha))
