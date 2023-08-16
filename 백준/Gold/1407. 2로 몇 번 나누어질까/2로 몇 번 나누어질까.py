a, b = map(int, input().split())


def func(num):
    cnt = num
    i = 2
    while i <= num:
        cnt += (num//i)*(i//2)
        i *= 2
    return cnt


print(func(b)-func(a-1))