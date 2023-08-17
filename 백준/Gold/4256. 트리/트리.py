from sys import stdin


def solve(s, e):
    global idx

    if s == e:
        print(inorder[s], end=' ')
        idx += 1
        return

    elif s > e:
        return

    root_index = inorder.index(preorder[idx])

    idx += 1
    solve(s, root_index - 1)

    solve(root_index + 1, e)
    print(inorder[root_index], end=' ')


for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    preorder = list(map(int, stdin.readline().split()))
    inorder = list(map(int, stdin.readline().split()))
    visited = set()

    idx = 0
    solve(0, n - 1)
    print()