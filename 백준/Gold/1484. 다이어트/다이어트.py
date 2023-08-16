from sys import stdin

g = int(stdin.readline())
ans = []

for now_weight in range(int(g ** 0.5), g + 1):
    if now_weight == 0:
        continue

    p1 = now_weight ** 2
    l, r = 0, now_weight

    while l < r:
        mid = (l + r) // 2
        if mid == 0:
            break
            
        res = p1 - mid ** 2
        if res < g:
            r = mid

        else:
            if res == g:
                ans.append(now_weight)
            l = mid + 1

if ans:
    for i in sorted(ans):
        print(i)
else:
    print(-1)