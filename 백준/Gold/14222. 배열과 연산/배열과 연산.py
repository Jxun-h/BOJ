from sys import stdin

n, k = map(int, stdin.readline().split())
nums = [x for x in range(1, n + 1)]
arr = list(map(int, stdin.readline().split()))


for i in sorted(arr):
    if i in nums:
        nums.remove(i)

    else:
        flag = False
        temp = i
        while 1:
            temp += k
            if temp in nums:
                flag = True
                break

            if temp > max(nums):
                break

        if flag:
            nums.remove(temp)

print(0 if nums else 1)