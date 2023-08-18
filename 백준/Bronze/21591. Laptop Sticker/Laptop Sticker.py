from sys import stdin

w1, h1, w2, h2 = map(int, stdin.readline().split())

print(1 if (w1-w2) >= 2 and (h1-h2) >=2 else 0)