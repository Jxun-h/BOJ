from sys import stdin

n = int(stdin.readline())
m, k = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))
arr.sort(reverse=True)

need_pens = m * k

cnt = 0
for i in range(n):
    if need_pens == 0:
        break

    if need_pens - arr[i] > -1:
        cnt += 1
        need_pens -= arr[i]

    elif need_pens - arr[i] < 0:
        cnt += 1
        need_pens -= arr[i]
        break

print("STRESS") if need_pens > 0 else print(cnt)