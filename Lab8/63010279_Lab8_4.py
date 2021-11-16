class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.index = 0
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.maxIndex = 0

    def insert(self, root, data):
        if root is None:
            return Node(data)
        else:
            if self.checkChild(root) == False:
                self.maxIndex +=1
                if root.left is None:
                    root.left = self.insert(root.left, data)
                    root.left.index = self.maxIndex
                else:
                    root.right = self.insert(root.right, data)
                    root.right.index = self.maxIndex
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

    def findIndex(self, node, index):
        if not node or node.index == index:
            return node
        else:
            if node.right and node.left:
                if self.findIndex(node.right, index) != None:
                    return self.findIndex(node.right, index)
                elif self.findIndex(node.left, index) != None:
                    return self.findIndex(node.left, index)
                else:
                    pass
            else:
                if node.right:
                    return self.findIndex(node.right, index)
                if node.left:
                    return self.findIndex(node.left, index)

    def comparepower(self, node1, node2):
        if self.sumTree(node1) > self.sumTree(node2):
            print(f'{node1.index}>{node2.index}')
        elif self.sumTree(node1) < self.sumTree(node2):
            print(f'{node1.index}<{node2.index}')
        else:
            print(f'{node1.index}={node2.index}')

    def checkChild(self, node):
        if node.left and node.right:
            return True
        return False

    def sumTree(self,node):
        if not node:
            return 0
        return node.data + self.sumTree(node.left) + self.sumTree(node.right)

if __name__ == "__main__":
    tree = BST()
    root = None
    power,order = input('Enter Input : ').split('/')
    power = power.split(' ')
    power = list(map(int,power))
    order = order.split(',')
    #จัดหน่วยอัศวิน
    for i in power:
        root = tree.insert(root,i)
    print(tree.sumTree(root))
    #วัดพลัง
    for i in order:
        first = tree.findIndex(root, int(i[0]))
        second = tree.findIndex(root, int(i[2]))
        tree.comparepower(first,second)