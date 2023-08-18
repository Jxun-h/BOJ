from sys import stdin

n = int(stdin.readline())
maximum = (n * 30)
a = [True for _ in range(maximum + 1)]
i = 2

while i < int(maximum ** 0.5):
    if a[i]:
        tmp = 2 * i
        while tmp <= maximum:
            a[tmp] = False
            tmp += i

    if i == 2:
        i -= 1
    i += 2

if n == 1:
    print(2)
else:
    j = 3
    cnt = 2

    check = False
    while not check:
        if cnt == n:
            check = True
        else:
            j += 2
            if a[j]:
                cnt += 1

    print(j)