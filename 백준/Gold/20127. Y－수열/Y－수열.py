from sys import stdin

n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))


def check_up():
    idx = -1
    cnt = 0
    for i in range(n - 1):
        if arr[i] > arr[i + 1]:
            idx = i
            cnt += 1
        if cnt > 1:
            return False

    if arr[-1] <= arr[0] or cnt == 0:
        return idx
    else:
        return False


def check_down():
    cnt = 0
    idx = -1
    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            idx = i
            cnt += 1
        if cnt > 1:
            return False

    if arr[-1] >= arr[0] or cnt == 0:
        return idx
    else:
        return False


# up
up_res = check_up()
# down
down_res = check_down()

if n == 1 or len(set(arr)) == 1:
    print(0)
    exit()

if up_res == -1 or down_res == -1:
    print(0)
else:
    if down_res is not False and up_res is not False:
        print(min(down_res + 1, up_res + 1))
    elif down_res is not False and up_res is False:
        print(down_res + 1)
    elif down_res is False and up_res is not False:
        print(up_res + 1)
    else:
        print(-1)
