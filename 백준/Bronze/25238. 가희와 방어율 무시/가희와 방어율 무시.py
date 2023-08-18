from sys import stdin

a, b = map(int, stdin.readline().split())
if b != 0:
    temp = a * (b / 100)
    res = a - temp
else:
    res = a
    
if res < 100:
    print(1)
else:
    print(0)