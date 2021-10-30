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

    def findMin(self):
        if self.root == None:
            return
        else:
            check = self.root
            while check.left != None:
                check = check.left
            return check.data
        

    def findMax(self):
        if self.root == None:
            return
        else:
            check = self.root
            while check.right != None:
                check = check.right
            return check.data

if __name__ == "__main__":
    T = BST()
    inp = [int(i) for i in input('Enter Input : ').split()]
    print(inp)
    for i in inp:
        root = T.insert(i)
    T.printTree(root)
    print("--------------------------------------------------")
    print(f'Min : {T.findMin()}')
    print(f'Max : {T.findMax()}')