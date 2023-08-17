from sys import stdin

n = int(stdin.readline())
temp = [0 for _ in range(n)]

for i in range(n):
    temp[i] = list(map(int, stdin.readline().split()))

Max_diff = 0
for i in range(1, n - 1):
    diff = (
                   abs(temp[i+1][0]-temp[i][0]) + abs(temp[i+1][1]-temp[i][1])
                   + abs(temp[i][0]-temp[i-1][0]) + abs(temp[i][1]-temp[i-1][1])
           ) - (
            abs(temp[i+1][0]-temp[i-1][0]) + abs(temp[i+1][1]-temp[i-1][1])
    )

    Max_diff = max(diff, Max_diff)

xtemp = temp[0][0]
ytemp = temp[0][1]
res = 0

for i in range(1, n):
    res += (abs(temp[i][0] - xtemp) + abs(temp[i][1] - ytemp))
    xtemp = temp[i][0]
    ytemp = temp[i][1]

print(res - Max_diff)