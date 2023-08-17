from sys import stdin

str1 = stdin.readline().rstrip()
str2 = stdin.readline().rstrip()
length1 = len(str1)
length2 = len(str2)

dp = [[0] * (length1 + 1) for _ in range(length2 + 1)]
answer = 0

for i in range(1, length2 + 1):
    for j in range(1, length1 + 1):
        if str2[i - 1] == str1[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
            answer = max(answer, dp[i][j])

print(answer)