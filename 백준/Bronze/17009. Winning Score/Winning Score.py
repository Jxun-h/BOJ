from sys import stdin
apple = 0
banana = 0

for team in range(2):
    for s in [3,2,1]:
        if team == 0:
            apple += int(stdin.readline()) * s
        else:
            banana += int(stdin.readline()) * s

if apple > banana:
    print('A')
elif apple < banana:
    print('B')
else:
    print('T')