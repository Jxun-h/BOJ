from sys import stdin

n, k = map(int, stdin.readline().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, stdin.readline().split())))

arr.sort(key=lambda x: (-x[1], -x[2], -x[3]))
grade = {x: [] for x in range(1, 501)}
num = 1
now = arr[0][1:]
grade[1].append(1)

for i in range(1, n):
    score = arr[i][1:]
    if score == now:
        grade[num].append(i + 1)
    else:
        num += 1
        grade[num].append(i + 1)
        now = arr[i][1:]

    if k - 1 == i:
        print(num)
        break