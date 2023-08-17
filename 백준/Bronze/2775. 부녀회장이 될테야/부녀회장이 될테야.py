from sys import stdin

arr = [[i for i in range(1, 16)] for _ in range(15)]
for i in range(1, 15):
    for j in range(15):
        if j == 0:
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i][j - 1] + arr[i - 1][j]

for _ in range(int(stdin.readline())):
    a = int(stdin.readline())
    b = int(stdin.readline())
    print(arr[a][b-1])