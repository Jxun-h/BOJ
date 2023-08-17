from sys import stdin

while 1:
    s = stdin.readline().rstrip('\n')
    if s == '***':
        break
    print(s[::-1])