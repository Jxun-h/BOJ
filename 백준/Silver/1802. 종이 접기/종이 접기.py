from sys import stdin


def check(str):
    todo = list(str)

    while len(todo) >= 3:
        for i in range(2, len(todo), 2):
            if todo[i-2] == todo[i]:
                return False

        nextTodo = []
        for i in range(1, len(todo), 2):
            nextTodo.append(todo[i])

        todo = nextTodo

    return True


for _ in range(int(stdin.readline())):
    data = str(stdin.readline().rstrip())

    if check(data):
        print("YES")
    else:
        print("NO")