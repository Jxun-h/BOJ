from sys import stdin

arr = [1, 2, 6, 24, 120]

n = int(stdin.readline())
if n < 5:
    print(0)
else:
    for i in range(6, 501):
        arr.append(arr[-1] * i)

    ans = 0
    s = str(arr[n-1])
    for i in range(len(s)-1, -1, -1):
        if s[i] == '0':
            ans += 1
        else:
            print(ans)
            break