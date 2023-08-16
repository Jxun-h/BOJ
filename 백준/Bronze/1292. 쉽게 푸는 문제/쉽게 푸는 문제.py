from sys import stdin
n,m=map(int,stdin.readline().split())
arr=[0,1]
for i in range(2,m+1):
    for j in range(i):
        arr.append(arr[-1]+i)
print(arr[m]-arr[n-1])