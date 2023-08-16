from sys import stdin
import math

ipt = stdin.readline

t = int(ipt().rstrip())

for step in range(t):
    cnt = 2
    x, y = ipt().split()
    x, y = int(x), int(y)
    mv_len = y-x
    sq_len = math.sqrt(mv_len)

    if sq_len != int(sq_len):
        i = 1
        while True:
            if pow(i, 2) > mv_len:
                break
            else: i += 1

        mid_len = (pow(i, 2) - pow(i-1, 2) - 1) / 2

        if pow(i - 1, 2) + mid_len >= mv_len:
            print(int(math.sqrt(pow(i - 1, 2)) * 2 - 1) + 1)
        else:
            print(int(math.sqrt(pow(i - 1, 2)) * 2 - 1) + 2)

    else:
        print(int(sq_len * 2 - 1))

