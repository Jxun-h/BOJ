from sys import stdin

l = int(stdin.readline())
string = stdin.readline().rstrip()
ans = 0
for i in range(l):
    n = ord(string[i]) - 96
    ans += n * (31 ** i)

print(ans % 1234567891)