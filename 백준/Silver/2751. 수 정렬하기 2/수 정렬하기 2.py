from sys import stdin

arr = []
for i in range(int(stdin.readline())):
    arr.append(int(stdin.readline()))

print(*sorted(arr), sep='\n')