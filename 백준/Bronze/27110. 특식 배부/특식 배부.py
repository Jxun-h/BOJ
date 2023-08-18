from sys import stdin

n = int(stdin.readline())
ans = 0

for i in list(map(int, stdin.readline().split())):
    if i < n:
        ans += i
    else:
        ans += n

print(ans)