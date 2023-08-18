import sys

input = sys.stdin.readline
n, k = map(int, input().split())


def f(x):
    return (x + 1) * (n - x + 1)


lo, hi = 0, n // 2 + 1
while lo != hi:
    mid = (lo + hi) >> 1
    if f(mid) == k:
        print("YES")
        sys.exit(0)
    if f(mid) > k:
        hi = mid
    else:
        lo = mid + 1

print("NO")