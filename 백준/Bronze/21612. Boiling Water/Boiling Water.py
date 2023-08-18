n = int(input())
res = 5 * n - 400
print(res)
if res < 100:
    print(1)
elif res > 100:
    print(-1)
else:
    print(0)