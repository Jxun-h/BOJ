from sys import stdin


n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
people = sum(arr)
max_value = max(arr)

if len(arr) == 1 and arr[0] == 1:
    print('Happy')

elif people - max_value < max_value:
    print('Unhappy')
else:
    print('Happy')