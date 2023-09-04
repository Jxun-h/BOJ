from sys import stdin


for i in range(int(stdin.readline().rstrip())):
    alphabet = {x for x in range(65, 91)}
    for j in list(stdin.readline().rstrip()):
        alphabet.discard(ord(j))

    print(sum(alphabet))