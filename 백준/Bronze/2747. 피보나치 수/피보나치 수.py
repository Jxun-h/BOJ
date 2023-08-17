from sys import stdin

n = int(stdin.readline())
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for i in range(18, 46):
    a.append(a[-1] + a[-2])

print(a[n])