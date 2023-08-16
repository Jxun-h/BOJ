from sys import stdin

n = int(stdin.readline())
limit = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
box = list(map(int, stdin.readline().split()))

limit.sort(reverse=True)
box.sort(reverse=True)

cnt = 0

if max(box) > max(limit):
    print(-1)
else:
    while box:
        if not box:
            break

        for l in limit:
            for b in box:
                if l >= b:
                    box.remove(b)
                    break
        cnt += 1
    print(cnt)