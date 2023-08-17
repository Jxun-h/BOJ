from sys import stdin, setrecursionlimit

setrecursionlimit(int(1e9))

t = int(stdin.readline())
n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
B = list(map(int, stdin.readline().split()))

Asum = {}
for i in range(n):
    for j in range(i, n):
        k = sum(A[i:j + 1])
        if k in Asum:
            Asum[k] += 1
        else:
            Asum[k] = 1

Bsum = {}
for i in range(m):
    for j in range(i, m):
        k = sum(B[i:j + 1])
        if k in Bsum:
            Bsum[k] += 1
        else:
            Bsum[k] = 1

res = 0

for key in Asum.keys():
    if (t - key) in Bsum:
        res += Bsum[t - key] * Asum[key]

print(res)