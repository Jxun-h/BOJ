from sys import stdin

n, w = int(stdin.readline()), sum(list(map(int, stdin.readline().split())))
print('yes' if w % 3 == 0 else 'no')