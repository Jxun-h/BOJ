from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
s, e = 0, n - 1
res = 1e9

while s < e:
    temp = arr[s] + arr[e]
    if abs(temp) < abs(res):
        res = temp

    if temp < 0:
        s += 1
    elif temp > 0:
        e -= 1
    else:
        break

print(res)
