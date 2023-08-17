from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
max_value = max(arr)
for i in range(n):
    arr[i] = arr[i] / max_value * 100

print(sum(arr) / n)