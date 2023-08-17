from sys import stdin

inp = stdin.readline
n, m = map(int, inp().split())
be, af = [], []

for i in range(n):
    res = ''
    s = stdin.readline().rstrip()
    for i in s:
        res += i * 2

    be.append(res)

for i in range(n):
    af.append(stdin.readline().rstrip())


def get_res():
    for i in range(n):
        if be[i] != af[i]:
            return 0

    return 1


print('Eyfa' if get_res() else 'Not Eyfa')
