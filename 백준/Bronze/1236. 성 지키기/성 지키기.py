from sys import stdin

n, m = map(int, stdin.readline().split())
arr = []
col = [False] * m
row = [False] * n
r1,r2 = 0,0

for i in range(n):
    data = list(stdin.readline().rstrip())
    arr.append(data)

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'X':
            row[i] = True
            col[j] = True

for i in range(n):
    if not row[i]:
        r1 += 1

for j in range(m):
    if not col[j]:
        r2 += 1

print(max(r1, r2))
