class Node:
    def __init__(self):
        self.right: Node | None = None
        self.left: Node | None = None
        self.key: int | None = None


class Tree:
    def __init__(self):
        self.root = Node()

    def add(self, x):
        el = self.root
        while el.key is not None:
            if el.key == x:
                return
            if x < el.key:
                if el.left is None:
                    el.left = Node()
                el = el.left
            else:
                if el.right is None:
                    el.right = Node()
                el = el.right

        el.key = x

    def rotate(self, x, command):
        el = self.root
        parent = None

        while el.key != x:
            parent = el
            if x < el.key:
                el = el.left
            else:
                el = el.right

        if command == "left":
            a = el.right
            el.right = a.left
            a.left = el
        else:
            a = el.left
            el.left = a.right
            a.right = el

        if parent is None:
            self.root = a
        elif parent.left is el:
            parent.left = a
        else:
            parent.right = a


def printt(self):
    stack = [self.root]

    while stack:
        el = stack.pop()
        if el is None:
            continue

        print(el.key, end=" ")
        stack.append(el.right)
        stack.append(el.left)
    print()


def main():
    tree = Tree()
    n = int(input())
    a = list(map(int, input().split()))
    for i in range(n):
        tree.add(a[i])

    m = int(input())
    for i in range(m):
        command = input().split()
        tree.rotate(int(command[1]), command[0])
        printt(tree)


main()
