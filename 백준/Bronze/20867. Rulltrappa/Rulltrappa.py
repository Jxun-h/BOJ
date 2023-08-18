from sys import stdin

m, s, g = map(float, stdin.readline().split())
a, b = map(float, stdin.readline().split())
l, r = map(float, stdin.readline().split())

fri = (1 / a) * l + m / g
lat = (1 / b) * r + m / s
print("friskus" if fri < lat else "latmask")