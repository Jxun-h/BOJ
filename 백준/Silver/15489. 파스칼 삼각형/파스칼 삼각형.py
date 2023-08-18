from sys import stdin

arr = [[1], [1, 1], [1, 2, 1]]
r, c, w = map(int, stdin.readline().split())

for i in range(4, 32):
    temp = [1]
    length = len(arr[-1])
    for i in range(length):
        if i == length - 1:
            temp.append(1)
        else:
            res = arr[-1][i] + arr[-1][i + 1]
            temp.append(res)
    arr.append(temp)

ans = 0
temp = c
for i in range(r - 1, r + w - 1):
    for j in range(c - 1, temp):
        k = arr[i][j]
        ans += k
    temp += 1

print(ans)