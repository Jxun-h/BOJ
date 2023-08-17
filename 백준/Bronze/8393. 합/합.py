from sys import stdin
ipt = stdin.readline
num = int(ipt())
result = 0
for step in range(1, num+1):
    result += step

print(result)