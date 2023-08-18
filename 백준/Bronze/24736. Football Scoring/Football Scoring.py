ans = []
a, b = list(map(int, input().split())), list(map(int, input().split()))
ans.append(a[0] * 6 + a[1] * 3 + a[2] * 2 + a[3] * 1 + a[4] * 2)
ans.append(b[0] * 6 + b[1] * 3 + b[2] * 2 + b[3] * 1 + b[4] * 2)
print(*ans)