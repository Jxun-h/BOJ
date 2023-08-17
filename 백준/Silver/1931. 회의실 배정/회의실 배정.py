from sys import stdin

ipt = stdin.readline
n = int(ipt().rstrip())

arr = []

for x in range(n):
    arr.append(list(map(int, ipt().split())))

arr.sort(key=lambda x:x[1])
idx = 0

while True:
    start = arr[idx][1]

    chk_same = 0
    for x in range(idx+1, n):
        if start == arr[x][1]:
            chk_same += 1
        else:
            break

    arr[idx:idx+chk_same+1] = sorted(arr[idx:idx+chk_same+1])
    idx += chk_same+1
    if idx == n:
        break

start = arr[0][1]

cnt = 0
for y in range(1, n):
    if start <= arr[y][0]:
        cnt += 1
        start = arr[y][1]

print(cnt+1)