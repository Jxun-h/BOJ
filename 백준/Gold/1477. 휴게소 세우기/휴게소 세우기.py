from sys import stdin


n, m, l = map(int, stdin.readline().split())
hyu = list(map(int, stdin.readline().split()))
hyu.append(0)
hyu.append(l)

hyu = sorted(hyu)

start = 1
end = l - 1
res = (start + end) // 2

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    if mid > 0:
        for i in range(1, len(hyu)):
            if hyu[i] - hyu[i-1] > mid:
                cnt += (hyu[i] - hyu[i - 1] - 1) // mid

        if cnt > m:
            start = mid + 1
        else:
            res = mid
            end = mid - 1
    else:
        res = end
        end = mid - 1

print(res)