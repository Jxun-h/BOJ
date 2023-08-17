from sys import stdin

n = int(stdin.readline())
nums = list(map(int, stdin.readline().split()))
dp = [0] * 400004
temp = 200001

answer = 0
for i in range(n):
    for j in range(i):
        if dp[nums[i] - nums[j] + temp] == 1:
            answer += 1
            break

    for k in range(i + 1):
        dp[nums[i] + nums[k] + temp] = 1

print(answer)
