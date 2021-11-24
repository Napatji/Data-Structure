class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.height = 1

    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
		# Perform normal BST
        if not root:
            return Node(key)
        elif int(key) < int(root.data):
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if abs(balance) > 1:
            if balance > 1 and int(key) < int(root.left.data):
                return self.rightRotate(root)

            if balance < -1 and int(key) >= int(root.right.data):
                return self.leftRotate(root)

            if balance > 1 and int(key) >= int(root.left.data):
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

            if balance < -1 and int(key) < int(root.right.data):
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
            # Perform rotation
        y.left = z
        z.right = T2
            # Update heights
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
            # Perform rotation
        y.right = z
        z.left = T3
            # Update heights
        z.height = 1 + max(self.getHeight(z.left),self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),self.getHeight(y.right))
            # Return the new root
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def printPreorder(self, node):
        if node != None:
            print(node.data,end=' ')
            self.printPreorder(node.left)
            self.printPreorder(node.right)

    def printInorder(self, node):
        if node != None:
            self.printInorder(node.left)
            print(node.data,end=' ')
            self.printInorder(node.right)

    def printPostorder(self, node):
        if node != None:
            self.printPostorder(node.left)
            self.printPostorder(node.right)
            print(node.data,end=' ')

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.data)
        printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    print(' *** AVL Tree ***')
    inp = input('Enter some numbers : ').split(' ')
    inp = list(map(int,inp))
    root = None
    for i in inp:
        root = T.insert(root,i)
    print(f'in_order  --> ',end='')
    T.printInorder(root)
    print(f'\npreorder  --> ',end='')
    T.printPreorder(root)
    print(f'\npostorder --> ',end='')
    T.printPostorder(root)