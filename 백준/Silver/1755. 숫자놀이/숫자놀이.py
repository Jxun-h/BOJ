from sys import stdin

d = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
     6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}

n, m = map(int, stdin.readline().split())
temp = []

for i in range(n, m + 1):
    data = list(str(i))
    s = []
    for j in range(len(data)):
        s.append(d[int(data[j])])
    s += [str(i)]
    temp.append(tuple(s))

temp.sort()
cnt = 0
for i in range(1, len(temp) + 1):
    if cnt < 10:
        print(temp[i-1][-1], end=' ')
    elif cnt == 10:
        print()
        print(temp[i - 1][-1], end=' ')
        cnt = 0
    cnt += 1
