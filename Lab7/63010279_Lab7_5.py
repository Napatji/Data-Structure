from os import truncate


class Stack:
    def __init__(self):
        self.value=[]
        self.score={'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}
    def push(self, value):
        self.value.append(value)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def isEmpty(self):
        if len(self.value)==0:
            return 1
        else:
            return 0
    def peek(self):
        return self.value[-1]
    def reverse(self):
        temp=[]
        for i in reversed(self.value):
            temp.append(i)
        self.value=temp

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
        self.stack = Stack()

    def toInorder(self, postfix):
        for i in postfix:
            if not isOperator(i):#เจอตัวเลข
                new_node = Node(i)
                self.stack.push(new_node)

            else:#เจอตัวดำเนินการ
                new_node = Node(i)#เก็บตัวดำเนินการเป็นNode
                #Popแล้วเก็บค่าตัวเลขที่จะดำเนินการ
                var1 = self.stack.pop()
                var2 = self.stack.pop()
                #นำตัวเลขไปเป็น Nodeลูกของตัวดำเนินการ
                new_node.right = var1
                new_node.left = var2
                #เพิ่มตัวดำเนินการลง Stack
                self.stack.push(new_node)
        #จับ Root มาเท่ากับตัวสุดท้ายที่เหลือซึ่งก็คือ Root
        self.root = self.stack.pop()
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def printInorder(self, node):
        if node != None:
            self.printInorder(node.left)
            print(node.data,end='')
            self.printInorder(node.right)

    def printPreorder(self, node):
        if node != None:
            print(node.data,end='')
            self.printPreorder(node.left)
            self.printPreorder(node.right)

def isOperator(value):
    if value in '+-*/^':
        return True
    else:
        return False

if __name__ == "__main__":
    T = BST()
    root = T.root
    inp = input('Enter Postfix : ') # Input
    # -------------------------Display-------------------------
    print('Tree :')
    root = T.toInorder(inp)
    T.printTree(root)
    print('--------------------------------------------------')
    print(f'Infix : ',end='')
    T.printInorder(root)
    print(end='\n')
    print(f'Prefix : ',end='')
    T.printPreorder(root)