from sys import stdin

ans = set()
for i in range(10):
    ans.add(int(stdin.readline()) % 42)

print(len(ans))