from sys import stdin

a, b = stdin.readline().rstrip().split()
a, b = int(a[::-1]), int(b[::-1])
print(a if a > b else b)