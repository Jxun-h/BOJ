from sys import stdin

while 1:
    try:
        n, m = map(int, stdin.readline().split())
        print(m // (n + 1))
    except:
        break