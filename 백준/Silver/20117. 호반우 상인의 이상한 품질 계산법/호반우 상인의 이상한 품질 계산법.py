from sys import stdin

n = int(stdin.readline())
ho_ban_woo = list(map(int, stdin.readline().split()))
ho_ban_woo.sort()

mid = n // 2
ans = ho_ban_woo[mid] * n

l, r = 0, n - 1
temp = 0

if n % 2 == 0:
    while l < r:
        temp += ho_ban_woo[r] * 2
        l += 1
        r -= 1

elif n % 2 != 0:
    for _ in range(n // 2):
        temp += ho_ban_woo[r] * 2
        l += 1
        r -= 1
    temp += ho_ban_woo[n // 2]

ans = max(ans, temp)
print(ans)
