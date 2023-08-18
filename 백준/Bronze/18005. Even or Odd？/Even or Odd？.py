from sys import stdin

n = int(stdin.readline())
if n % 2 == 1:
    ans = 0
elif n // 2 % 2 == 0:
    ans = 2
else:
    ans = 1

print(ans)