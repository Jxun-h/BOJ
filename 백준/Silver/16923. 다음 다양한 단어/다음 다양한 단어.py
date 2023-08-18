from sys import stdin

s = list(stdin.readline().rstrip())
pos_alpha = [0 for _ in range(26)]
length = len(s)
idx = 0

while idx < length:
    pos_alpha[ord(s[idx]) - 97] = idx + 1
    idx += 1


def solve(s):
    if idx < 26:
        for i in range(26):
            if not pos_alpha[i]:
                s.append(chr(i + 97))
                print(*s, sep='')
                return
    else:
        for i in range(25, -1, -1):
            for j in range(ord(s[i]) - 97 + 1, 26):
                if pos_alpha[ord(s[i]) - 97] < pos_alpha[j]:
                    s[i] = chr(j + 97)
                    s = s[:i+1]
                    print(*s, sep='')
                    return

    print(-1)
    return


solve(s)