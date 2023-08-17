from sys import stdin

ans = 0
for _ in range(int(stdin.readline())):
    stack = []
    s = stdin.readline().rstrip()

    for i in s:
        if not stack:
            stack.append(i)

        elif stack[-1] != i:
            stack.append(i)

        elif stack[-1] == i:
            stack.pop()

    if not stack:
        ans += 1

print(ans)