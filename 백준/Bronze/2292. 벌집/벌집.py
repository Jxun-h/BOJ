from sys import stdin

n = int(stdin.readline())
cnt = 1
if n == 1:
    print(cnt)
else:
    start, end = 2, 7
    p1, p2 = 6, 12

    while 1:
        if start <= n <= end:
            print(cnt + 1)
            break

        cnt += 1
        start += p1
        end += p2
        p1 += 6
        p2 += 6