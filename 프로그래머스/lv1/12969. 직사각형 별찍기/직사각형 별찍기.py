a, b = map(int, input().strip().split(' '))
for x in range(0, b):
    star = ""
    for y in range(0,a):
        star += '*'
    print(star)