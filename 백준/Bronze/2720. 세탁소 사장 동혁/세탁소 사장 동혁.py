from sys import stdin

for _ in range(int(stdin.readline())):
    c = int(stdin.readline())
    coin = [25, 10, 5, 1]
    for i in range(4):
        print(int(c // coin[i]), end=' ')
        c %= coin[i]
    print()