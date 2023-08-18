from sys import stdin

x1, y1, r1 = map(int, stdin.readline().split())
x2, y2, r2 = map(int, stdin.readline().split())
d = (x1 - x2) ** 2 + (y1 - y2) ** 2
print('YES' if (r1 + r2) ** 2 > d else 'NO')
