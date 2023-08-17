from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().split()))
    res = -int(1e9)
    for i in range(n):
        temp = arr[i]
        if res < temp:
            res = temp
        for j in range(i + 1, n):
            temp += arr[j]
            if temp > res:
                res = temp
    print(res)