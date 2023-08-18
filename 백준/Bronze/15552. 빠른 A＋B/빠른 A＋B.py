from sys import stdin
ipt = stdin.readline
num = int(ipt().rstrip())

for step in range(num):
    a, b = ipt().split()
    a, b = int(a), int(b)

    print(a+b)