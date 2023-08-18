from sys import stdin

n = int(stdin.readline().rstrip())
x = 2

if n == 1:
    pass

else:
    while 1:
        if n == 1:
            break

        if n % x == 0:
            print(x)
            n /= x
        else:
            x += 1