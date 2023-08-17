from sys import stdin

ipt = stdin.readline

num = int(ipt().rstrip())

for step in range(num):
    cnt = 0

    arr = list(map(int, ipt().rstrip().split()))

    average = sum(arr[1:]) / arr[0]

    for x in range(1, len(arr)):
        if arr[x] > average:
            cnt += 1

    print('%.3f%%' % (cnt / len(arr[1:]) * 100))