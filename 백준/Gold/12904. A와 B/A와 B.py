from sys import stdin

s = list(stdin.readline().rstrip())
t = list(stdin.readline().rstrip())

tf = False

while t:
    if t[-1] == 'A':
        t.pop()
    else:
        t.pop()
        t.reverse()

    if s == t:
        tf = True
        break

print(0) if not tf else print(1)