from sys import stdin

n, k, q = map(int, stdin.readline().split())

for i in range(q):
    l, h = map(int, stdin.readline().split())
    if k == 1:
        print(abs(l - h))
        continue

    cnt = 0
    while l != h:
        while l > h:
            cnt += 1
            l = (l + k - 2) // k

        while h > l:
            cnt += 1
            h = (h + k - 2) // k

    print(cnt)