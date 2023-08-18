from math import sqrt
from sys import stdin

n, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
answer = int(1e9)


def get_val(m, l):
    res = 0

    for i in l:
        res += (i - m) ** 2

    return res / len(l)


res_list = []

for i in range(n - k + 1):
    for j in range(n - k - i + 2):
        temp = arr[i:i + k + j]
        m = sum(temp) / len(temp)
        res = get_val(m, temp)
        res_list.append(res)

answer = min(res_list)

print(sqrt(answer))