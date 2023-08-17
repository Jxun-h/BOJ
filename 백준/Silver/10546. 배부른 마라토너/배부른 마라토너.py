from sys import stdin

n = int(stdin.readline())
mara_tang = {}

for _ in range(n):
    name = stdin.readline().rstrip()
    if name not in mara_tang:
        mara_tang[name] = 1
    else:
        mara_tang[name] += 1

for _ in range(n - 1):
    mara_tang[stdin.readline().rstrip()] -= 1

for key, item in mara_tang.items():
    if item != 0:
        print(key)
        break