from sys import stdin

n = int(stdin.readline().rstrip())
nums = list(map(int, stdin.readline().rstrip("\n").split()))

sum_val = 0

sum_list = []

if n == 1:
    nums = sorted(nums)
    for i in range(0, 5):
        sum_val += nums[i]
else:
    sum_list.append(min(nums[0], nums[5]))
    sum_list.append(min(nums[1], nums[4]))
    sum_list.append(min(nums[2], nums[3]))
    sum_list = sorted(sum_list)

    min1 = sum_list[0]
    min2 = sum_list[0] + sum_list[1]
    min3 = sum_list[0] + sum_list[1] + sum_list[2]

    n1 = (n - 2) * (n - 2) + 4 * (n - 1) * (n - 2)
    n2 = 4 * (n - 2) + 4 * (n - 1)
    n3 = 4

    sum_val += n1 * min1
    sum_val += n2 * min2
    sum_val += n3 * min3

print(sum_val)
