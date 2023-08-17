from sys import stdin

n = int(stdin.readline())
_1, _2 = 0, 0
flag = 0

for _ in range(n):
    data = stdin.readline().rstrip().split()
    team = int(data[0])
    m, s = map(int, data[1].split(':'))

    if team == 1:
        if flag == 0:
            _1 += 48 * 60 - (60 * m + s)
        flag += 1

        if flag == 0:
            if _2 > 0:
                _2 -= (48 * 60 - (60 * m + s))
    else:
        if flag == 0:
            _2 += 48 * 60 - (60 * m + s)
        flag -= 1
        if flag == 0:
            if _1 > 0:
                _1 -= (48 * 60 - (60 * m + s))

print("{:0>2}:{:0>2}".format(_1 // 60, _1 % 60))
print("{:0>2}:{:0>2}".format(_2 // 60, _2 % 60))
