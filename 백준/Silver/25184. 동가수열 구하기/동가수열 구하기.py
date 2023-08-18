from sys import stdin

n = int(stdin.readline())
sub_ = int(n / 2)
arr = []
i = 1

while i + sub_ <= n:
    arr.append(i + sub_)
    if i not in arr:
        arr.append(i)
    i += 1

print(*arr)
