class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
    
    def __str__(self):
        return str(self.data)

class Stack:
    def __init__(self):
        self.value = []
    def push(self, data):
        self.value.append(data)
    def pop(self):
        if self.value:
            temp = self.value[-1]
            self.pop()
            return temp
    def peek(self):
        if self.value:
            return self.value[-1]

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root == None:
            self.root = Node(data)
        else:
            priority = {'^':4,'/':3,'*':2,'+':1,'-':0}
            check_node = self.root
            while True:
                if priority['^'] == data:
                    pass
                elif priority['/'] == data:
                    pass
                elif priority['*'] == data:
                    pass
                elif priority['+'] == data:
                    pass
                elif priority['-'] == data:
                    pass

        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

if __name__ == "__main__":
    T = BST()
    inp = [i for i in input('Enter Postfix : ')]
    operator = Stack()
    for info in inp:
        if info in '()^*/+-':
            operator.push(info)
    priority = {'^':4,'/':3,'*':2,'+':1,'-':0}
    temp = operator.value
    for i in temp:
         root = T.insert(priority[i])
    T.printTree(root)