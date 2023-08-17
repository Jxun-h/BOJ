from sys import stdin
ipt = stdin.readline

num = int(ipt().rstrip())

for x in range(num):
    a, b = ipt().rstrip().split()
    a, b = int(a), int(b)
    print('Case #{}: {} + {} = {}'.format(x+1, a, b, a+b))

