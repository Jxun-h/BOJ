from sys import stdin

s = list(map(int, list(stdin.readline().rstrip())))

string = '' + str(s[0])
cnt = 0

for i in range(1, len(s)):
    if s[i - 1] == s[i] - 1:
        string += str(s[i])
    else:
        if len(string) == 3:
            cnt += 1
        string = ''
        string += str(s[i])

if len(string) == 3:
    cnt += 1

print(cnt)