import sys
sys.setrecursionlimit(int(1e6))


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


pre = []
post = []


def preorder(node, nodeinfo):
    pre.append(nodeinfo.index(node.data) + 1)
    if node.left:
        preorder(node.left, nodeinfo)
    if node.right:
        preorder(node.right, nodeinfo)


def postorder(node, nodeinfo):
    if node.left:
        postorder(node.left, nodeinfo)

    if node.right:
        postorder(node.right, nodeinfo)

    post.append(nodeinfo.index(node.data) + 1)


def solution(nodeinfo):
    new_node = sorted(nodeinfo, key=lambda k: -k[1])

    root = None
    for node in new_node:
        if not root:
            root = Tree(node)
        else:
            current = root
            while 1:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break

                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

                break

    preorder(root, nodeinfo)
    postorder(root, nodeinfo)

    return [pre, post]