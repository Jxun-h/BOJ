from sys import stdin

n, m = map(int, stdin.readline().split())
nums = []
now = 0


def solve(start, end, target):
    while end > start:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid
    return end


for _ in range(n):
    count = int(stdin.readline())
    nums.append(now + count - 1)
    now += count
nums.append(int(1e12))

for _ in range(m):
    j = int(stdin.readline())
    it = solve(0, len(nums), j)
    print(it + 1)
