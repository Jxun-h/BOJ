from sys import stdin

t, s = map(int, stdin.readline().split())
spe, ans = '', 0
if t < 12:
    spe = 'm'
elif 11 < t < 17:
    spe = 'l'
else:
    spe = 'd'

if s or not spe == 'l':
    ans = 280
elif spe == 'l' and not s:
    ans = 320

print(ans)