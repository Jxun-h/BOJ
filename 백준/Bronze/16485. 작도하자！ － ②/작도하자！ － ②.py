from sys import stdin

c, b = map(int, stdin.readline().rstrip().split())

print('%.7f' % (c / b))