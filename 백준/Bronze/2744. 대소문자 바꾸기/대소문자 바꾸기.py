from sys import stdin
s = stdin.readline().rstrip()
answer = ''
for i in s:
    if i.isupper():
        answer += i.lower()
    else:
        answer += i.upper()
print(answer)