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

    def insert(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            check_node = self.root
            while True:
                if check_node.data <= val:
                    if check_node.right:
                        check_node = check_node.right
                    else:
                        check_node.right = Node(val)
                        break
                elif check_node.data > val:
                    if check_node.left:
                        check_node = check_node.left
                    else:
                        check_node.left = Node(val)
                        break
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
    
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

T = BST()
print(' *** Binary Search Tree ***')
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print(' ')
print(' --- Tree traversal ---')
print('Preorder : ',end='')
T.printPreorder(root)
print('\n',end='')
print('Inorder : ',end='')
T.printInorder(root)
print('\n',end='')
print('Postorder : ',end='')
T.printPostorder(root)
print('\n',end='')
T.printTree(root)
