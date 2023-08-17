from sys import stdin

arr = list(map(int, stdin.readline().split()))
if arr == list(range(1, 9)):
    print('ascending')
elif arr == list(range(8, 0, -1)):
    print('descending')
else:
    print('mixed')
