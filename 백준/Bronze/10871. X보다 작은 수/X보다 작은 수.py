from sys import stdin

n, m = map(int, stdin.readline().split())
for i in list(map(int, stdin.readline().split())):
    if m > i:
        print(i, end=' ')
