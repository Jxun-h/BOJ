from sys import stdin

x, y = map(int, stdin.readline().split())
a, b = 100 - x, 100 - y
c, d = 100 - (a + b), a * b
q, r = d // 100, d % 100
front, back = c + q, r
print(a, b, c, d, q, r)
print(front, back)