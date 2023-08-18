from sys import stdin

n, L = map(int, stdin.readline().split())
arr = list(map(int, stdin.readline().split()))

temp = 0
tf = True

for i in range(n - 1, 0, -1):
    temp += arr[i]
    if not(arr[i-1] - L < temp / (n - i) < arr[i-1] + L):
        print('unstable')
        exit()

print('stable')