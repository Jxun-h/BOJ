from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

l, h = map(int, stdin.readline().split())
s = []
answer = 0


def solve(length, nums):
    if length == len(nums):
        res = int(''.join(nums))
        if l <= res <= h:
            global answer
            answer += 1

        return

    for i in ['4', '7']:
        solve(length, nums + [i])


for i in range(len(str(l)), len(str(h)) + 1):
    solve(i, s)

print(answer)