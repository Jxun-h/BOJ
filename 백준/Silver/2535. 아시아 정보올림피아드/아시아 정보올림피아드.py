from sys import stdin

n = int(stdin.readline())
grade = []
for i in range(n):
    a,b,c = map(int, stdin.readline().split())
    grade.append((c, a, b))

h = {}

grade.sort(reverse=True)
cnt = 0
for i in range(n):
    if cnt == 3:
        break
    
    if grade[i][1] not in h:
        print(*grade[i][1:])
        cnt += 1
        h[grade[i][1]] = 1
    else:
        if h[grade[i][1]] < 2:
            print(*grade[i][1:])
            h[grade[i][1]] += 1
            cnt += 1
        else:
            continue
