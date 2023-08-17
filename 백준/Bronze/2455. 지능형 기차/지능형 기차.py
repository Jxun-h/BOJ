from sys import stdin

ans, res = 0, 0
for i in range(4):
    leave, on = map(int, stdin.readline().split())
    res += -1 * leave + on
    ans = max(res, ans)
    
print(ans)