from sys import stdin
ipt = stdin.readline
A, B, C = ipt().rstrip().split()

if int(B) >= int(C):
    print(-1)
else:
    sonic_price = int(A) / (int(C) - int(B))
    print(int(sonic_price) + 1)