from sys import stdin

arr = stdin.readline().rstrip()
cnt = 0
point = [0 for _ in range(26)]
for i in arr:
    point[ord(i) - 97] += 1


def solve(goal, p):
    global cnt
    if goal == 0:
        cnt += 1
        return

    for c in set(list(arr)):
        if point[ord(c) - 97] > 0 and c != p:
            point[ord(c) - 97] -= 1
            solve(goal - 1, c)
            point[ord(c) - 97] += 1


solve(len(arr), '')
print(cnt)