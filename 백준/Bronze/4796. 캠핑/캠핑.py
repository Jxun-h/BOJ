from sys import stdin
c = 0
while 1:
    c += 1
    l, p, v = map(int, stdin.readline().split())
    if l == p == v == 0:
        break
    print('Case {}:'.format(c), (v // p) * l + min((v % p), l))