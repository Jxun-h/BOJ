from sys import stdin, setrecursionlimit
setrecursionlimit(10**7)

per, k = map(int, stdin.readline().split())
s = list(stdin.readline().rstrip())
ans = 0
for i in range(per):
    if s[i] == 'P':
        for j in range(i - k, i + k + 1):
            if -1 < j < per:
                if s[j] == 'H':
                    s[j] = 'X'
                    ans += 1
                    break

print(ans)