from sys import stdin

s = int(stdin.readline())
ans, res, num = 0, 0, 1

while res < s:
    res += num
    num += 1
    ans += 1

print(ans if res == s else ans - 1)