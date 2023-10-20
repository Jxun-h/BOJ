from sys import stdin

arr = []
for x in range(int(stdin.readline())):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key=lambda x: (x[0], x[1]))
x1, x2 = arr[0][0], arr[-1][0]

arr.sort(key=lambda x: (x[1], x[0]))
y1, y2 = arr[0][1], arr[-1][1]

print(((x2 - x1) * (y2 - y1)))