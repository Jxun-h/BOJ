from sys import stdin

string = list(stdin.readline().rstrip())
ans = ''

for i in range(0, len(string)):
    ans = min(ans + string[i], string[i] + ans)

print(ans)