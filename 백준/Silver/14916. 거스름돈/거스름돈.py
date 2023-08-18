from sys import stdin

n = int(stdin.readline())
res = int(1e9)

for i in range(n // 5, -1, -1):
    money = n - i * 5
    cnt = i
    if money % 2 != 0:
        continue
    else:
        cnt += money // 2

    res = min(cnt, res)

print(res) if res != int(1e9) else print(-1)