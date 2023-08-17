from sys import stdin
a = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]

for _ in range(9990):
    a.append(a[-2] + a[-1])
    
print(a[int(stdin.readline())])