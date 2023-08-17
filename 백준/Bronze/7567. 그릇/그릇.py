from sys import stdin

state = ''
data = stdin.readline().rstrip()
res = 0

for i in data:
    if state == '':
        res += 10
        state = i
        
    elif state == i:
        res += 5
        
    else:
        res += 10
        state = i
        
print(res)  