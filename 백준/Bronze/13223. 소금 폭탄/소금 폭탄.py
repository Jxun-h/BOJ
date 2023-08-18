import datetime

a = list(map(int, input().rstrip().split(':')))
b = list(map(int, input().rstrip().split(':')))
s_time = a[0] * 3600 + a[1] * 60 + a[2]
e_time = b[0] * 3600 + b[1] * 60 + b[2]

if s_time >= e_time:
    e_time += 24 * 3600

res = e_time - s_time

h = res // 3600
res %= 3600

m = res // 60
res %= 60

print('%02d:%02d:%02d' % (h, m, res))