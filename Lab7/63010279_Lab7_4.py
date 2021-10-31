class Node:
    def __init__(self, data): 
        self.data = data  
        self.left = None  
        self.right = None 
        self.level = None 

    def setLevel(self, num):
        self.level = num

    def __str__(self):
        return str(self.data) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None
        self.max_level = 0

    def insert(self, val):  
        self.max_level += 1
        if self.root == None:
            self.root = Node(val)
            self.root.level = 0
        else:
            check_node = self.root
            level = 0
            while True:
                if check_node.data < val:
                    if check_node.right:
                        check_node = check_node.right
                        level += 1
                    else:
                        level += 1
                        check_node.right = Node(val)
                        check_node.right.level = level
                        break
                elif check_node.data >= val:
                    if check_node.left:
                        check_node = check_node.left
                        level += 1
                    else:
                        level += 1
                        check_node.left = Node(val)
                        check_node.left.level = level
                        break
        return self.root
        
    def delete(self,root, data):
        check_node = root
        if check_node is None:#ไม่มี Root
            print(f'Error! Not Found DATA')
        else:#มี Root
            parent_node = None#Pointerชี้พ่อแม่ Node ที่จะลบ
            while True:
                if check_node is None:#ไม่มี data ที่จะลบใน Root
                    print(f'Error! Not Found DATA')
                    break
                elif data > check_node.data:#มากกว่าไปขวา
                    parent_node = check_node
                    check_node = check_node.right
                elif data < check_node.data:#น้อยกว่าไปซ้าย
                    parent_node = check_node
                    check_node = check_node.left
                elif data == check_node.data:
                    if parent_node is None: #แสดงว่าลบ Root
                        parent_node = self.root
                        if check_node.right and check_node.left:#มีลูก 2 
                            check_node = check_node.right
                            min_node, parent_node = checkLeftMin(check_node, parent_node)
                            temp = min_node.data #เก็บ data node ที่จะมาแทน Root
                            if min_node.right:
                                self.delete(root,min_node)
                                self.root.data = temp
                                break
                            elif min_node.right is None:
                                if parent_node == self.root:
                                    parent_node.right = None
                                else:
                                    parent_node.left = None
                                self.root.data = temp
                                break
                        elif check_node.right or check_node.left:#มีลูกเดี่ยว
                            if check_node.right:
                                check_node = check_node.right
                                self.root = check_node
                            elif check_node.left:
                                check_node = check_node.left
                                self.root = check_node 
                            break     
                        elif check_node.right is None and check_node.left is None:#ไม่มีลูก
                            self.root = None
                            break

                    else:#ลบตั้งแต่ Root ลงไป
                        if check_node.right and check_node.left:#มีลูก 2 
                            replace_node = check_node
                            check_node = check_node.right
                            min_node, parent_node = checkLeftMin(check_node, parent_node)
                            temp = min_node.data #เก็บ data node ที่จะมาแทน Root
                            if min_node.right:
                                self.delete(root,min_node.data)
                                replace_node.data = temp
                                break
                            elif min_node.right is None: 
                                parent_node.left = None
                                replace_node.data = temp
                                break
                        elif check_node.right or check_node.left:#มีลูกเดี่ยว
                            if parent_node.right == check_node:
                                if check_node.right:
                                    check_node = check_node.right
                                    parent_node.right = check_node
                                elif check_node.left:
                                    check_node = check_node.left
                                    parent_node.right = check_node
                            elif parent_node.left == check_node:
                                if check_node.right:
                                    check_node = check_node.right
                                    parent_node.left = check_node
                                elif check_node.left:
                                    check_node = check_node.left
                                    parent_node.left = check_node
                            break 
                        elif check_node.right is None and check_node.left is None:#ไม่มีลูก
                            if parent_node.left == check_node:
                                parent_node.left = None
                            elif parent_node.right == check_node:
                                parent_node.right = None
                            break
        return self.root

def checkLeftMin(node, parent):
    check = node
    parent_node = parent
    while check.left:
        parent_node = check
        check = check.left
    return check,parent_node
    
def checkRightMost(node, parent):
    check = node
    parent_node = parent
    while check.right:
        parent_node = check
        check = check.right
    return check,parent_node

def printTree90(node, level = 0):
    if node != None:
        printTree90(node.right, level + 1)
        print('     ' * level, node)
        printTree90(node.left, level + 1)

if __name__ == "__main__":
    tree = BinarySearchTree()
    data = input("Enter Input : ").split(",")
    for i in data:
        if i[0] == 'i':
            root = tree.insert(int(i[1:]))
            print(f'insert{i[1:]}')
            printTree90(root)
        if i[0] == 'd':
            print(f'delete{i[1:]}')
            root = tree.root
            root = tree.delete(root, int(i[1:]))
            printTree90(root)