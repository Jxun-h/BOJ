from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    a, b = stdin.readline().rstrip().split()
    arr.append((a, int(b)))

arr.sort(key=lambda x: x[1])
print(arr[0][0])