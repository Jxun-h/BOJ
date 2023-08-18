from sys import stdin


def chk():
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if c == a * i + b * j and f == d * i + e * j:
                return i, j


arr = list(map(int, stdin.readline().split()))
a, b, c = arr[:3]
d, e, f = arr[3:]

x, y = chk()
print(x, y)