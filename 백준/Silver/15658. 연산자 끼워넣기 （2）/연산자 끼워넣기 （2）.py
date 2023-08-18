from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
n_num = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))


def dfs(num, val):
    global max_res, min_res
    if not num:
        max_res = max(val, max_res)
        min_res = min(val, min_res)
        return
    else:
        for i in range(4):
            if i == 0:
                if arr[i] > 0:
                    arr[i] -= 1
                    dfs(num[1:], val + num[0])
                    arr[i] += 1

            elif i == 1:
                if arr[i] > 0:
                    arr[i] -= 1
                    dfs(num[1:], val - num[0])
                    arr[i] += 1

            elif i == 2:
                if arr[i] > 0:
                    arr[i] -= 1
                    dfs(num[1:], val * num[0])
                    arr[i] += 1

            elif i == 3:
                if arr[i] > 0:
                    arr[i] -= 1
                    if val < 0:
                        temp = abs(val) // num[0] * -1
                    else:
                        temp = val // num[0]
                    dfs(num[1:], temp)
                    arr[i] += 1


max_res = -int(1e9)
min_res = int(1e9)
dfs(n_num[1:], n_num[0])
print(max_res, min_res, sep='\n')