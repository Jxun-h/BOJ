from sys import stdin

N, K = map(int, stdin.readline().split())
li = list(stdin.readline().rstrip())

k, stack = K, []

for i in range(N):
    while k > 0 and stack and stack[-1] < li[i]:
        stack.pop()
        k -= 1
    stack.append(li[i])
print(''.join(stack[:N-K]))