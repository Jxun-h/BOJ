from sys import stdin

n, m = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
for i in range(1, n):
    arr[i] += arr[i - 1]

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    print(arr[b - 1] - (arr[a - 2] if a - 2 > -1 else 0))