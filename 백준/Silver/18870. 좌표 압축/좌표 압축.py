from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))

temp = list(set(arr))
temp.sort()

d = {temp[x]:x for x in range(len(temp))}


for i in arr:
    print(d[i], end=' ')