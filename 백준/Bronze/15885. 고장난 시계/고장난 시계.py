from sys import stdin

a, b = map(int, stdin.readline().rstrip().split())
print('%d' % (abs(a / b - 1) * 2))