from sys import stdin
a = ['a','e','i','o','u']

for i in range(int(stdin.readline())):
    s = stdin.readline().rstrip().lower().replace(" ", '')
    ans1 = 0
    for j in a:
        ans1 += s.count(j)

    print(len(s) - ans1, ans1)
