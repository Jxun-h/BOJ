from sys import stdin
ipt = stdin.readline
N = int(ipt().rstrip())
arr = []

for x in range(N):
    arr.append(int(ipt().rstrip()))

arr = sorted(arr, reverse=True)

weight = idx = 1

for x in range(len(arr)):
    if idx == 1:
        chk = arr[:idx][0]
    else:
        chk = arr[idx-1:idx][0] * idx
    if weight < chk:
        weight = chk
        idx += 1
    else:
        idx += 1

print(weight, end='')