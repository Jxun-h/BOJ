from sys import stdin
idx = 0
while 1:
    o, w = map(int, stdin.readline().split())
    if o == 0 and w == 0:
        quit()
    tf = True

    while 1:
        a, b = stdin.readline().rstrip().split()
        if a == '#' and b == '0':
            break

        if tf:
            if a == 'F':
                w += int(b)
            elif a == 'E':
                w -= int(b)

        if w <= 0:
            tf = False

    idx += 1
    if w <= 0:
        print("%d RIP" % idx)
    elif o / 2 < w < o * 2:
        print("%d :-)" % idx)
    else:
        print("%d :-(" % idx)