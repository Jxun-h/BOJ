from sys import stdin

n, a, b = map(int, stdin.readline().split())
w, h = max(n - a, a), max(n - b, b)
print(w * h * 4)