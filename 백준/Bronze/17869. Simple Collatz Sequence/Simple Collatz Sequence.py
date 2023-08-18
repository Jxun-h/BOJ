from sys import stdin

n = int(stdin.readline())
ans = 0
while n!=1:
    n = n + 1 if n % 2 != 0 else n // 2
    ans += 1
print(ans)