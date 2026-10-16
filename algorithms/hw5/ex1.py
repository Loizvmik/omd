class Node:
    def __init__(self):
        self.right: Node | None = None
        self.left: Node | None = None
        self.key: int | None = None
        
class Tree:
    def __init__(self):
        self.root = Node()
        self.root.left = Node() 
        self.root.right = Node()
        

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

    def exists(self,x):
        el = self.root
        while el is not None and el.key is not None:
            if el.key > x:
                el = el.left
            elif el.key < x:
                el=el.right
            else:
                return "YES"
        return "NO"

    def delete(self, x):
        el = self.root
        parent = None
        while el is not None and el.key is not None:
            if el.key > x:
                parent = el
                el = el.left
            elif el.key < x:
                parent = el
                el = el.right
            else:
                if el.right is None or el.right.key is None:
                    if el.left is None or el.left.key is None:
                        a = None
                    else:
                        a = el.left
                else:
                    if el.left is None or el.left.key is None:
                        a = el.right
                    else:
                        parent_a = el
                        a = el.right
                        while a.left is not None and a.left.key is not None:
                            parent_a = a
                            a = a.left
                        el.key = a.key
                        if parent_a is el:
                            parent_a.right = a.right
                        else:
                            parent_a.left = a.right
                        return

                if parent is None:
                    self.root = a if a is not None else Node()
                elif parent.left is el:
                    parent.left = a
                else:
                    parent.right = a
                return



    def height(self):
        stack = [(self.root, 1)]
        height = 0
    
        while stack:
            el, depth = stack.pop()
            if el is None or el.key is None:
                continue
    
            height = max(height, depth)
            stack.append((el.right, depth + 1))
            stack.append((el.left, depth + 1))
    
        return height
        

def printt(self):
    stack = [self.root]
    if self.root.key is None:
        print("Empty")
        return
        
    while stack:
        el = stack.pop()
        if el is None or el.key is None:
            continue

        print(el.key, end=" ")
        stack.append(el.right)
        stack.append(el.left)
    print()


def main():
    tree = Tree()
    n = int(input())
    for i in range(n):
        command = input().split()
        if command[0] == "add":
            tree.add(int(command[1]))
        elif command[0] == "del":
            tree.delete(int(command[1]))
        elif command[0] == "exists":
            print(tree.exists(int(command[1])))
        elif command[0] == "height":
            print(tree.height())
        elif command[0] == "print":
            printt(tree)


main()
