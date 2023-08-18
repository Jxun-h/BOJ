from sys import stdin

a, b = map(int, stdin.readline().split())


def solve(a, b):
    if a == b:
        return 0

    if a < b:
        return b - a

    cnt = 0
    while a > b:
        if a % 2 == 0:
            a //= 2

        else:
            a += 1

        cnt += 1

    return b - a + cnt


print(solve(a, b))
