from sys import stdin

n, m = map(int, stdin.readline().split())
active_memory = [0] + list(map(int, stdin.readline().split()))
off_cost_memory = [0] + list(map(int, stdin.readline().split()))

sum_cost_memory = sum(off_cost_memory)
dp = [[0] * (sum(off_cost_memory) + 1) for _ in range(n + 1)]
result = sum(off_cost_memory)

for i in range(1, n + 1):
    act_mem = active_memory[i]
    off_mem = off_cost_memory[i]

    for j in range(1, sum_cost_memory + 1):
        if j < off_mem:
            dp[i][j] = dp[i - 1][j]

        else:
            dp[i][j] = max(act_mem + dp[i - 1][j - off_mem], dp[i - 1][j])

        if dp[i][j] >= m:
            result = min(result, j)

print(result)
