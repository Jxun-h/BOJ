from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 6)

n = int(stdin.readline())
arr = [0]

for _ in range(n):
    arr.append(int(stdin.readline()))

ans = set()


def dfs(fir, sec, num):
    fir.add(num)
    sec.add(arr[num])
    if arr[num] in fir:
        if fir == sec:
            ans.update(fir)
            return 1
        return 0
    return dfs(fir, sec, arr[num])


for i in range(1, n + 1):
    if i not in ans:
        dfs(set(), set(), i)

print(len(ans))
print(*sorted(ans), sep='\n')