from sys import stdin
from fractions import Fraction

n, m = map(int, stdin.readline().split())
juice = []

for _ in range(n):
    juice.append(tuple(map(int, stdin.readline().split())))

juice.sort(key=lambda x: (x[0] / x[1]), reverse=True)

res = 0

while m != 0 and juice:
    juice_w, juice_v = juice.pop()

    if juice_w <= m:
        m -= juice_w
        res += Fraction(juice_v, 1)

    else:
        res += Fraction(m * juice_v, juice_w)
        m = 0

answer = str(res)
if '/' in answer:
    print(answer)
else:
    print(answer + '/1')