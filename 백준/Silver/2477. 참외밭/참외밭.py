from sys import stdin

n = int(stdin.readline())
nums = []
x, y = [], []
for _ in range(6):
    direction, length = map(int, stdin.readline().split())
    nums.append(length)
    if direction == 1 or direction == 2:
        x.append(length)
    else:
        y.append(length)

max_x = max(x)
max_y = max(y)
xi = nums.index(max_x)
yi = nums.index(max_y)

if xi + 1 >= 6:
    x = abs(nums[xi - 1] - nums[0])
else:
    x = abs(nums[xi - 1] - nums[xi + 1])

if yi + 1 >= 6:
    y = abs(nums[yi - 1] - nums[0])
else:
    y = abs(nums[yi - 1] - nums[yi + 1])

print(((max_x * max_y) - (x * y)) * n)