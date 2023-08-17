from sys import stdin

btn = [0, 0, 0]
a, b, c = 300, 60, 10
t = int(stdin.readline())

if t % 10 != 0:
    print(-1)

else:
    btn[0] += t // a
    t %= a

    btn[1] += t // b
    t %= b

    btn[2] += t // c
    print(*btn)