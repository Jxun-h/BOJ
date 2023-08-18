from sys import stdin

n = int(stdin.readline())
stack = list(map(int, stdin.readline().split()))
stack.sort()
temp = []

while stack:
    if not temp:
        temp.append(stack.pop())

    if temp[-1] / 2 + stack[0] > temp[-1] + stack[0] / 2:
        data = temp[-1] / 2 + stack[0]
    else:
        data = temp[-1] + stack[0] / 2

    temp.pop()
    stack.pop(0)
    temp.append(data)

ans = temp[0]
print(int(ans) if ans % 10 == 0 else ans)