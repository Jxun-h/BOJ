while 1:
    a = float(input())
    if a == 0:
        break
    print("%.2f" % (1 + a + pow(a, 2) + pow(a, 3) + pow(a, 4)))