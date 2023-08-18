import sys
ipt = sys.stdin.readline
x, y = int(ipt()), int(ipt())

if x > 0 and y > 0:
    print(1)
elif x > 0 > y:
    print(4)
elif x < 0 < y:
    print(2)
else:
    print(3)