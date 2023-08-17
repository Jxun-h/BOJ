from sys import stdin

nums = list(map(int, stdin.readline().split()))


def clock_num(num):
    min_val = int(''.join(map(str, num)))
    for i in range(1, 4):
        temp = int(''.join(map(str, num[i:] + num[:i])))
        if min_val > temp:
            min_val = temp
    return min_val


cn = clock_num(nums)
ans = 1
for i in range(1111, cn):
    if '0' not in list(str(i)) and i == clock_num(list(map(int, str(i)))):
        ans += 1

print(ans)