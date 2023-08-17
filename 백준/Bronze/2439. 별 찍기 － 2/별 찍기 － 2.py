from sys import stdin

n = int(stdin.readline())
for i in range(1, n + 1):
    space = ' ' * (n - i)
    print(space + ('*' * i))