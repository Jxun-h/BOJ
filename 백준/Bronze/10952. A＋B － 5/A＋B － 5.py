from sys import stdin

while 1:
    n, m = map(int, stdin.readline().split())
    if n == 0 == m:
        break
        
    print(n + m)