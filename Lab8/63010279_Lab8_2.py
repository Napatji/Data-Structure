class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class AVL:
    def __init__(self):
        self.root = None

    def insert(self, data):
        #Code here.
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = AVL()
    inp = input('Enter Input : ').split(' ')
    for i in inp:
        root = T.insert(i)
        print(f'Insert : ( {i} )')
        T.printTree(root)
        print('--------------------------------------------------')