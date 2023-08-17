from sys import stdin

int(stdin.readline())
a = list(map(int, stdin.readline().split()))
print(min(a), max(a))
