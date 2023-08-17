from sys import stdin

s = stdin.readline().rstrip()
answer = [0, 0]
idx = 0

while len(s) - 3 >= idx:
    if s[idx: idx + 3] == 'JOI':
        answer[0] += 1

    elif s[idx: idx + 3] == 'IOI':
        answer[1] += 1

    idx += 1

print(*answer, sep='\n')