from sys import stdin

n, k = map(int, stdin.readline().split())
length, ans = 0, 0
arr = [0 for _ in range(1000000)]

for _ in range(n):
    g, x = map(int, stdin.readline().split())
    length = max(length, x)
    arr[x] = g

res = sum(arr[:k * 2 + 1])
ans = res

for i in range(k * 2 + 1, length + 1):
    res += (arr[i] - arr[i - (k * 2 + 1)])
    ans = max(ans, res)

print(ans)
