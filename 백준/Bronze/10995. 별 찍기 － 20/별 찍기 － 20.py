from sys import stdin

n = int(stdin.readline())
if n == 1:
    print('*')
else:
    p1, p2 = '', ' '
    for i in range(n):
        p1 += '*'
        if i != n - 1:
            p1 += ' '
        
        p2 += '*'
        if i != n - 1:
            p2 += ' '
            
    for i in range(n):
        if i % 2 == 0:
            print(p1)
        else:
            print(p2)