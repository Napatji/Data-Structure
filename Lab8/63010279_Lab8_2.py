class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

    def __str__(self):
        return str(self.val)

class AVL_Tree(object):

    def __init__(self):
        self.root = None

    def insert(self, root, key):
		# Perform normal BST
        if not root:
            return TreeNode(key)
        elif int(key) < int(root.val):
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.getHeight(root.left),self.getHeight(root.right))

        balance = self.getBalance(root)

        if abs(balance) > 1:
            if balance > 1 and int(key) < int(root.left.val):
                return self.rightRotate(root)

            if balance < -1 and int(key) >= int(root.right.val):
                return self.leftRotate(root)

            if balance > 1 and int(key) >= int(root.left.val):
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)

            if balance < -1 and int(key) < int(root.right.val):
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

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.val)
        printTree(node.left, level + 1)

if __name__ == "__main__":
    T = AVL_Tree()
    root = None
    inp = input('Enter Input : ').split(' ')
    for i in inp:
        root = T.insert(root, i)
        print(f'Insert : ( {i} )')
        printTree(root)
        print('--------------------------------------------------')
    # print(T.getBalance(root))
    # print(T.getBalance(root.left))
    # # print(T.getHeight(root.left))
    # # print(T.getHeight(root.right))
    # # print(root.height)