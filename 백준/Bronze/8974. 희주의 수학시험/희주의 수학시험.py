from sys import stdin

arr, res = [], 0
a, b = map(int, stdin.readline().split())
for i in range(1, 50):
    cnt = 0
    while cnt != i:
        arr.append(i)
        cnt += 1

for i in range(a, b + 1):
    res += arr[i-1]

print(res)