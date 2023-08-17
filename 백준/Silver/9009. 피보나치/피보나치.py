from sys import stdin

fibo = [0, 1, 1, 2, 3]
while 1:
    if fibo[-1] + fibo[-2] > int(1000000000):
        break
    fibo.append(fibo[-1] + fibo[-2])

for tc in range(int(stdin.readline())):
    data = int(stdin.readline())
    answer = [50, []]
    temp = []
    cnt = 0

    for i in range(len(fibo) - 1, 0, -1):
        if data - fibo[i] >= 0:
            data -= fibo[i]
            cnt += 1
            temp.append(fibo[i])

    temp.sort()
    print(*temp)