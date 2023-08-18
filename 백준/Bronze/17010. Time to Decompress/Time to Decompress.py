from sys import stdin
for _ in range(int(stdin.readline())):
    n, s = stdin.readline().split()
    print(s * int(n))