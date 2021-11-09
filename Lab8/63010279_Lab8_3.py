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

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if self.checkChild(root) == False:
                if root.left is None:
                    root.left = self.insert(root.left, data)
                else:
                    root.right = self.insert(root.right, data)
            else:
                if self.checkChild(root.left) == False:
                    self.insert(root.left, data)
                elif self.checkChild(root.right) == False:
                    self.insert(root.right, data)
                elif self.checkChild(root.left) == True and self.checkChild(root.right) == True:
                    self.insert(root.left, data)
        return root

    def checkChild(self, node):
        if node.left and node.right:
            return True
        return False

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)      

def printTree(node, level = 0):
    if node != None:
        printTree(node.right, level + 1)
        print('     ' * level, node.data)
        printTree(node.left, level + 1)

if __name__ == "__main__":
    tree = BST()
    root = None
    node_number,node_value = input('Enter Input : ').split('/')
    node_value = node_value.split(' ')
    # if (int(node_number) // 2) + 1 != len(node_value):
    #     print('Incorrect Input')
    if int(node_number) < 3:
        print('Incorrect Input')
    else:
        for i in range(1,int(node_number)+1):
            root = tree.insert(root, i)
        # for i in node_value:
        #     root = tree.insert(root, int(i))
    printTree(root)