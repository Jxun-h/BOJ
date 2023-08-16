from sys import stdin

s = stdin.readline().rstrip()
data = s + ''.join(reversed(s[:-1]))
ans = len(s) * 2

for i in range(1, len(s) + 1):
    temp = s + ''.join(reversed(s[:-i]))
    length = len(temp)
    mid = length // 2

    if length % 2 == 0:
        if temp[:mid] == ''.join(reversed(temp[mid:])):
            ans = min(ans, length)

    else:
        if temp[:mid] == ''.join(reversed(temp[mid + 1:])):
            ans = min(ans, length)

print(ans)