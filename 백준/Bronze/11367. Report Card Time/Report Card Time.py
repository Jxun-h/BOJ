from sys import stdin


def check(g):
    res = ''
    if 97 <= g <= 100:
        res = 'A+'
    elif 90 <= g <= 96:
        res = 'A'
    elif 87 <= g <= 89:
        res = 'B+'
    elif 80 <= g <= 86:
        res = 'B'
    elif 77 <= g <= 79:
        res = 'C+'
    elif 70 <= g <= 76:
        res = 'C'
    elif 67 <= g <= 69:
        res = 'D+'
    elif 60 <= g <= 66:
        res = 'D'
    elif 0 <= g <= 59:
        res = 'F'

    return res


for _ in range(int(stdin.readline())):
    name, grade = stdin.readline().rstrip().split()
    ans = check(int(grade))
    print(name, ans)