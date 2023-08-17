from sys import stdin

n, m = map(int, stdin.readline().split())
arr = {}

for _ in range(m):
    a, b = map(int, stdin.readline().split())
    if a not in arr:
        arr[a] = [b]
    else:
        arr[a].append(b)

    if b not in arr:
        arr[b] = [a]
    else:
        arr[b].append(a)

for i in range(1, n + 1):
    if i in arr:
        print(len(arr[i]))
    else:
        print(0)