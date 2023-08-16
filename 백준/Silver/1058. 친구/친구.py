from sys import stdin

n = int(stdin.readline())
arr = []
for i in range(n):
    temp = stdin.readline().rstrip().replace("N", '0').replace("Y", '1')
    data = list(map(int, list(temp)))
    arr.append(data)

res = [0] * n
test = [item[:] for item in arr]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if arr[i][k] and arr[k][j]:
                    test[i][j] = 1

res = 0
for i in range(n):
    friends = sum(test[i])
    if res < friends:
        res = friends

print(res)