from sys import stdin

for _ in range(int(stdin.readline())):
    a = list(stdin.readline().rstrip().split())
    print(*(a[2:] + a[:2]))
