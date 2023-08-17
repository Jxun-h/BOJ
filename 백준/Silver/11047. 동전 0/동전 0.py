from sys import stdin

ipt = stdin.readline

arr = ipt().split()
n, k = int(arr[0]), int(arr[1])
coin_list = []
cnt = 0

for x in range(n):
    coin_list.append(int(ipt().rstrip()))

for coin in reversed(coin_list):
    if k == 0:
        break

    elif coin > k:
        continue

    else:
        cnt += k // coin
        k = k % coin

print(cnt)
