from sys import stdin

n = int(stdin.readline())
arr = []
for _ in range(n):
    arr.append(stdin.readline().rstrip())

for i in arr:
    for j in arr:
        if i == j[::-1]:
            print(len(i), i[len(i)//2])
            exit()