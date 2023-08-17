from sys import stdin
while 1:
    n, k = map(int, stdin.readline().split())
    if n == 0 and k == 0:
        break
    sub_nk, a, b = n - k, 1, 1
    for i in range(n, max(k, sub_nk), -1):
        a *= i
    for i in range(1, min(k, sub_nk) + 1):
        b *= i
    print(a // b)