from sys import stdin

for _ in range(int(stdin.readline())):
    hp, mp, s, d, _hp, _mp, _s, _d = map(int, stdin.readline().split())
    hp = hp + _hp if hp + _hp > 0 else 1
    mp = mp + _mp if mp + _mp > 0 else 1
    s = s + _s if s + _s > -1 else 0
    d = d + _d
    
    print(1 * hp + 5 * mp + 2 * s + 2 * d)
    