from sys import stdin
arr = list(map(int, stdin.readline().split()))
ans = 0
for i in arr:
    ans += i ** 2

print(ans % 10)