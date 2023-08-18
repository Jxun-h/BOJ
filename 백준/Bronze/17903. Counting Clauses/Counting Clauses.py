m, n = map(int, input().split())
check = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    a = 1 if a > 0 else 0
    b = 1 if a > 0 else 0
    c = 1 if a > 0 else 0    
    if (not a or b or c) and (not a or not b or c) and (a or not b or c) \
        and (a or not b or not c) and (a or b or c) and m >= 8:
        check = 1
print("satisfactory" if check else "unsatisfactory")