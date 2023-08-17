from sys import stdin

n = int(stdin.readline())
arr = [0, 1, 0, 1, 1] + [0] * (n - 4)

for i in range(5, n + 1):
    if 0 in [arr[i - 1], arr[i - 4], arr[i - 3]]:
        arr[i] = 1
    else:
        arr[i] = 0

print('SK' if arr[n] else 'CY')