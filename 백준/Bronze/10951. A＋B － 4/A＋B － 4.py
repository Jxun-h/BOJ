from sys import stdin

while 1:
    try:
        n, m = map(int, stdin.readline().split())
        print(n + m)
    except:
        break