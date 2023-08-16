import sys

# input() 함수보다 좀 더 빠름
ipt = sys.stdin.readline

num = sorted(list(str(int(ipt()))), reverse=True)

result = ''
for step in num:
    result += step

print(int(result))