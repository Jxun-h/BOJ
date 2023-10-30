from sys import stdin

while (1):
    a = float(stdin.readline())
    if a == -1.0:
        break
    print("Objects weighing {:.2f} on Earth will weigh {:.2f} on the moon.".format(a, round(a * 0.167, 2)))
