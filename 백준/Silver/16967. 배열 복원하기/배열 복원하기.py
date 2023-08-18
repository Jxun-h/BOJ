from sys import stdin

h, w, x, y = map(int, stdin.readline().split())
A = []
B = []

for _ in range(h + x):
    B.append(list(map(int, stdin.readline().split())))

for i in range(h - (h - x)):
    A.append(B[i][:w])

for i in range(x, h):
    data = B[i]
    temp = []
    for j in range(w):
        if j - y < 0:
            temp.append(B[i][j])
        else:
            temp.append(B[i][j] - A[i - x][(j - y)])

    A.append(temp)

for i in A:
    print(*i)