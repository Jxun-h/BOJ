from sys import stdin

x, y = map(int, stdin.readline().split())

if x == y == 0:
    print('Not a moose')
elif x != y:
    k = max(x, y)
    print('Odd %d' % (k * 2))
else:
    print('Even %d' % (x + y))