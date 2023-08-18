from sys import stdin

n, m = map(int, stdin.readline().split())

for _ in range(n):
    print(stdin.readline().rstrip()[::-1])