from sys import stdin

n = int(stdin.readline())
a, b = map(int, stdin.readline().split())
print(min(a // 2 + b, n))