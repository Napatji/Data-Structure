class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            check = self.root
            while True:
                if check.data > data:
                    if check.left == None:
                        check.left = Node(data)
                        break
                    else:
                        check = check.left
                elif check.data <= data:
                    if check.right == None:
                        check.right = Node(data)
                        break
                    else:
                        check = check.right
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(type(root))
T.printTree(root)