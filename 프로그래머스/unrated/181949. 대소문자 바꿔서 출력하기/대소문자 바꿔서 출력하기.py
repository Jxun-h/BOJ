str = input()
for i in str:
    if i.islower():
        print(i.upper(), end="")
        continue
    print(i.lower(), end="")