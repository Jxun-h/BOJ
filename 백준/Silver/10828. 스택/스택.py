from sys import stdin

stack = []

for i in range(int(stdin.readline())):
    k = list(stdin.readline().split())
    if len(k) == 1:
        if k[0] == 'top':
            if stack:
                print(stack[-1])
            else:
                print(-1)
        elif k[0] == 'size':
            print(len(stack))

        elif k[0] == 'empty':
            if stack:
                print(0)
            else:
                print(1)
        elif k[0] == 'pop':
            if stack:
                print(stack.pop())
            else:
                print(-1)
    else:
        stack.append(k[1])
