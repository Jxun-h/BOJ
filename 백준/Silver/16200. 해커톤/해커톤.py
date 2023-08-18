from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
base, limit, ans = 0, 0, 0
arr.sort()

while base < n:
    limit = arr[base]

    while limit > 0:
        limit -= 1
        base += 1
    ans += 1

print(ans)