from sys import stdin

n = int(stdin.readline())
h = list(stdin.readline().rstrip())
stack = []
alpha = {}

for i in range(1, n + 1):
    alpha[chr(64 + i)] = int(stdin.readline())

for i in h:
    if i.isalpha():
        stack.append(alpha[i])

    else:
        a = stack.pop()
        b = stack.pop()

        if i == '+':
            stack.append(b + a)

        elif i == '-':
            stack.append(b - a)

        elif i == '*':
            stack.append(b * a)

        else:
            stack.append(b / a)

print("%.2f" % stack[0])