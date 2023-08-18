from sys import stdin


def solve(x):
    mod = 1000000007
    a = 2
    b = x
    ret = 1
    while b:
        if b % 2 == 1:
            ret *= a
            ret %= mod

        a *= a
        a %= mod
        b //= 2

    return ret


for _ in range(int(stdin.readline())):
    test_data = int(stdin.readline())
    if 0 < test_data < 2:
        print(1)

    else:
        x = test_data - 2
        print(solve(x))
