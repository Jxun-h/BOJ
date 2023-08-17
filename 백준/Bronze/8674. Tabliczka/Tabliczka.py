from sys import stdin
a, b = map(int, stdin.readline().split())

if a % 2 != 0 and b % 2 != 0:
    print(min(a, b))
else:
    print(0)