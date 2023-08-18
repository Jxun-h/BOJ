from sys import stdin
n, w = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(int(stdin.readline()))

m = False
coin = 0
for i in range(n - 1):
    if not m and arr[i] < arr[i + 1]:
        m = arr[i]
        coin = w // m
        w -= coin * m

    elif m and arr[i] > arr[i + 1]:
        w += arr[i] * coin
        coin, m = 0, False

if m:
    w += coin * arr[-1]

print(w)