
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
            print('*')
        else:
            check = self.root
            while True:
                if check.data >= data:
                    print('L',end='')
                    if check.left == None:
                        check.left = Node(data)
                        break
                    else:
                        check = check.left
                elif check.data < data:
                    print('R',end='')
                    if check.right == None:
                        check.right = Node(data)
                        break
                    else:
                        check = check.right
            print('*')
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
    def checkTree(self, number, check_node = None):
        if check_node == None:
            check = self.root
            if check.data > number:
                check.data = check.data*3
            if check.right:
                self.checkTree(number, check.right)
            if check.left:
                self.checkTree(number, check.left)
        else:
            check = check_node
            if check.data > number:
                check.data = check.data*3
            if check.right:
                self.checkTree(number, check.right)
            if check.left:
                self.checkTree(number, check.left)

if __name__ == "__main__":
    T = BST()
    inp = input('Enter Input : ').split(' ')
    for i in inp:
        root = T.insert(int(i))
    # T.printTree(root)