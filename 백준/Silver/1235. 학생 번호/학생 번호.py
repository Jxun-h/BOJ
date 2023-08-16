from sys import stdin, setrecursionlimit


n = int(stdin.readline())
nums = []
for _ in range(n):
    nums.append(stdin.readline().rstrip())

for i in range(1, len(nums[0]) + 1):
    res = {}
    for j in range(n):
        data = nums[j][-i:]
        if data in res:
            break
        else:
            res[data] = 1

    if len(res) == n:
        print(i)
        break