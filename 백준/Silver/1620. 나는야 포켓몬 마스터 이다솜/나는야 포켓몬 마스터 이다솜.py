from sys import stdin

a, b = {},{}
n, m = map(int, stdin.readline().split())
for i in range(1, n + 1):
    c = stdin.readline().rstrip()
    a[c] = i
    b[i] = c

for _ in range(m):
    d = stdin.readline().rstrip()
    if d.isdigit():
        print(b[int(d)])
    else:
        print(a[d])