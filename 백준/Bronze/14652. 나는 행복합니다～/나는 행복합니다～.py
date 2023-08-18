from sys import stdin

n, m, k = map(int, stdin.readline().rstrip().split())

print(k//m, k%m)