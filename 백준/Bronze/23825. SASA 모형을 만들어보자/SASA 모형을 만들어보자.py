from sys import stdin
n, m = map(int, stdin.readline().split())
print(min(n // 2, m // 2))