from sys import stdin

ipt = stdin.readline

sugar_kg = int(ipt().rstrip())
_05kg = sugar_kg // 5
temp_kg = sugar_kg

if temp_kg != 0:
    while temp_kg != 0:
        if _05kg < 0:
            print(-1)
            break

        temp_kg -= _05kg * 5
        if temp_kg % 3 == 0:
            _03kg = temp_kg // 3
            print(_05kg + _03kg)
            temp_kg -= _03kg * 3

        else:
            temp_kg = sugar_kg
            _05kg -= 1
else:
    print(-1)