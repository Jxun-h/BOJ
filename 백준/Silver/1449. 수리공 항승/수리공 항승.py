from sys import stdin

n, l = map(int, stdin.readline().split())
sep = 0.5
arr = list(map(int, stdin.readline().split()))
arr.sort()
start, ans = arr[0], 1
end = start + l - sep

for i in arr:
    if end >= i:
        continue
    ans += 1
    end = i + l - sep

print(ans)
