from sys import stdin
from math import factorial


def get_res(n):
    return factorial(2*n) // (factorial(n) * factorial(n + 1))


dp = [0 for _ in range(5001)]
dp[2] = 1

for _ in range(int(stdin.readline().strip())):
    L = int(stdin.readline().strip())
    if L % 2 != 0:
        print(0)
        continue

    res = get_res(L // 2)
    dp[L] = res
    print(res % 1000000007)
