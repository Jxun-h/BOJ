from sys import stdin
n = list(map(int, stdin.readline().split()))
n.sort()
print(n[1])