from sys import stdin


n = int(stdin.readline())
arr = stdin.readline().rstrip()
tf = True

for i in range(n - 4):
    tf = True
    for j in range(i + 1, i + 5):
        if arr[j - 1] == 'A' and ord(arr[j - 1]) + 1 == ord(arr[j]):
            continue

        if arr[j - 1] == 'Z' and ord(arr[j - 1]) - 1 == ord(arr[j]):
            continue

        if ord(arr[j - 1]) + 1 == ord(arr[j]) or ord(arr[j - 1]) - 1 == ord(arr[j]):
            continue
        else:
            tf = False

    if tf:
        break

print('YES' if tf else 'NO')
