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
                else:
                    self.insert(self.findAlmostLeft(root), data)
        return root

    def findAlmostLeft(self, node):
        find = node
        if not find.left.left:
            return node
        else:
            return self.findAlmostLeft(find.left)

    def checkChild(self, node):
        if node.left and node.right:
            return True
        return False

    def subtract(self, root):
        if not root:
            return
        left = root.left
        right = root.right
        if self.checkChild(left) == False and self.checkChild(right) == False:
            temp_L = left.data
            temp_R = right.data
            root.data = int(min(temp_L,temp_R))
            left.data = int(temp_L) - int(min(temp_L,temp_R))
            right.data = int(temp_R) - int(min(temp_L,temp_R))
        if self.checkChild(left) == True and self.checkChild(right) == True:
            left = self.subtract(left)
            right = self.subtract(right)
            temp_L = left.data
            temp_R = right.data
            root.data = int(min(temp_L,temp_R))
            left.data = int(temp_L) - int(min(temp_L,temp_R))
            right.data = int(temp_R) - int(min(temp_L,temp_R))
        if self.checkChild(left) == True and self.checkChild(right) == False:
            left = self.subtract(left)
            temp_L = left.data
            temp_R = right.data
            root.data = int(min(temp_L,temp_R))
            left.data = int(temp_L) - int(min(temp_L,temp_R))
            right.data = int(temp_R) - int(min(temp_L,temp_R))
        if self.checkChild(left) == False and self.checkChild(right) == True:
            right = self.subtract(right)
            temp_L = left.data
            temp_R = right.data
            root.data = int(min(temp_L,temp_R))
            left.data = int(temp_L) - int(min(temp_L,temp_R))
            right.data = int(temp_R) - int(min(temp_L,temp_R))
        return root

def sumTree(node):
    if  node != None:
        pass

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
    if (int(node_number) // 2) + 1 != len(node_value):
        print('Incorrect Input')
    if int(node_number) < 3:
        print('Incorrect Input')
    else:
        for i in range(1,int(node_number)+1):
            if i < len(node_value):
                root = tree.insert(root, 0)
            else:
                root = tree.insert(root, int(node_value[i-len(node_value)]))