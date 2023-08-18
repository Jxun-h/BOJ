from sys import stdin
data = stdin.readline().rstrip()
answer = 0
if len(data) == 1:
    print(answer)
else:
    res = 1
    while len(data) != 1:
        for i in data:
            res *= int(i)
            
        answer += 1
        data = str(res)
        res = 1
    print(answer)