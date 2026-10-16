class Node:
    def __init__(self):
        self.right: Node | None = None
        self.left: Node | None = None
        self.key: int | None = None
        self.height = 0


class Tree:
    def __init__(self):
        self.root = Node()

    def get_height(self, el):
        if el is None:
            return 0
        return el.height

    def update_height(self, el):
        el.height = 1 + max(
            self.get_height(el.left), self.get_height(el.right)
        )

    def balance(self, el):
        return self.get_height(el.right) - self.get_height(el.left)

    def rotate(self, el, command):
        if command == "left":
            a = el.right
            el.right = a.left
            a.left = el
        else:
            a = el.left
            el.left = a.right
            a.right = el

        self.update_height(el)
        self.update_height(a)
        return a

    def add(self, x):
        el = self.root
        stack = []
        while el.key is not None:
            if el.key == x:
                return
            stack.append(el)
            if x < el.key:
                if el.left is None:
                    el.left = Node()
                el = el.left
            else:
                if el.right is None:
                    el.right = Node()
                el = el.right

        el.key = x
        el.height = 1

        while stack:
            el = stack.pop()
            self.update_height(el)
            a = el

            if self.balance(el) == 2:
                if self.balance(el.right) < 0:
                    el.right = self.rotate(el.right, "right")
                a = self.rotate(el, "left")
            elif self.balance(el) == -2:
                if self.balance(el.left) > 0:
                    el.left = self.rotate(el.left, "left")
                a = self.rotate(el, "right")

            if not stack:
                self.root = a
            else:
                parent = stack[-1]
                if parent.left is el:
                    parent.left = a
                else:
                    parent.right = a

    def exists(self, x):
        el = self.root
        while el is not None and el.key is not None:
            if el.key > x:
                el = el.left
            elif el.key < x:
                el = el.right
            else:
                return "YES"
        return "NO"

    def height(self):
        return self.root.height


def printt(self):
    if self.root.key is None:
        print("Empty")
        return

    stack = [self.root]
    a = []
    while stack:
        el = stack.pop()
        if el is None:
            continue

        a.append(el.key)
        stack.append(el.right)
        stack.append(el.left)
    print(*a)


def main():
    tree = Tree()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == "add":
            tree.add(int(command[1]))
        elif command[0] == "exists":
            print(tree.exists(int(command[1])))
        elif command[0] == "root":
            if tree.root.key is None:
                print("Empty")
            else:
                print(tree.root.key)
        elif command[0] == "height":
            print(tree.height())
        elif command[0] == "print":
            printt(tree)


main()
