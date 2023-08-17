from sys import stdin
ipt = stdin.readline
global Map

def print_stars(N):
    if N == 3:
        Map[0][:3] = Map[2][:3] = [1] * 3
        Map[1][:3] = [1, 0, 1]
        return

    num = N // 3
    print_stars(num)

    for x in range(3):
        for y in range(3):
            if x == 1 and y == 1:
                continue
            for z in range(num):
                Map[num * x + z][num * y:num*(y+1)] = Map[z][:num]


N = int(ipt().rstrip())
Map = [[0 for i in range(N)] for i in range(N)]

print_stars(N)

for x in Map:
    for y in x:
        if y:
            print('*', end='')
        else:
            print(' ', end='')
    print()