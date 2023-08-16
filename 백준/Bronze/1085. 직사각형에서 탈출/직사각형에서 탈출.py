from sys import stdin

x, y, w, h = map(int, stdin.readline().split())
y_min, x_min = int(1e9), int(1e9)
y_min = min(abs(h - y), y_min, x)
x_min = min(abs(w - x), x_min, y)

print(min(x_min, y_min))