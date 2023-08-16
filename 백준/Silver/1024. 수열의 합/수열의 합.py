from sys import stdin

n, l = map(int, stdin.readline().split())
start = 0
temp = ((l + 1) * l) // 2 - l

while 1:
    if l > 100:
        print(-1)
        break

    if temp == n:
        for i in range(start, start + l):
            print(i, end=' ')
        break
    elif temp > n:
        l += 1
        temp = ((l + 1) * l) // 2 - l
        start = 0

    else:
        k = (n - temp) // l
        temp += k * l
        start += k
        if k == 0 and temp != n:
            temp += l