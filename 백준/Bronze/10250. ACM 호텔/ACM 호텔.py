from sys import stdin

for _ in range(int(stdin.readline())):
    h, w, n = map(int, stdin.readline().split())
    if n % h == 0:
        print(str(h) + '%.2d' % (n // h))
    else:
        print(str(n % h) + '%.2d' % (n // h + 1))