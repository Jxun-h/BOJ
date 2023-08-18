from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
tf = 0

if sum(arr) % 3 == 0:
    temp = 0
    for i in arr:
        temp += i // 2

    if temp >= sum(arr) // 3:
        tf = 1

print('YES' if tf else 'NO')