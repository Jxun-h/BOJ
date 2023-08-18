from sys import stdin

n = int(stdin.readline())
arr= list(map(int, stdin.readline().split()))
stat, ans= 0, 0

for i in range(n):
    if arr[i] == stat:
        ans += 1

        if stat < 2:
            stat += 1
        else:
            stat = 0

print(ans)