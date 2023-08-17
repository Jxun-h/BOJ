from sys import stdin, setrecursionlimit
setrecursionlimit(int(1e9))
k = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
res = [[] for _ in range(k)]


def binary_separation(arr, depth):
    if len(arr) == 1:
        res[depth].extend(arr)
        return

    length = len(arr)
    mid = length // 2
    res[depth].append(arr[mid])
    binary_separation(arr[:mid], depth + 1)
    binary_separation(arr[mid + 1:], depth + 1)


binary_separation(arr, 0)

for i in range(k):
    if i == 0:
        print(res[i][0])
    else:
        print(*res[i])