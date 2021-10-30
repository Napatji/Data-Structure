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
        if root == None:
            print(f'Error! Not Found DATA')
        else:
            parent = None
            check_node = root
            while True:
                if check_node is None:
                    print(f'Error! Not Found DATA')
                    break
                if data > check_node.data:
                    parent = check_node
                    check_node = check_node.right
                elif data < check_node.data:
                    parent = check_node
                    check_node = check_node.left
                elif data == check_node.data:
                    #delete node(no child)
                    if check_node.left is None and check_node.right is None:
                        if parent is None:
                            self.root = None
                        else:
                            if parent.left == check_node:
                                parent.left = None
                            elif parent.right == check_node:
                                parent.right = None
                        break
                    #delete node(with 2 child)
                    elif check_node.left and check_node.right:
                        if parent or parent is None:
                            #delete root
                            parent = check_node
                            minimumParent = None
                            check_node = check_node.right
                            if check_node.left is None:
                                parent.data = check_node.data
                                parent.right = None
                                break
                            while check_node.left:
                                minimumParent = check_node
                                check_node = check_node.left
                            temp = check_node.data
                            if check_node.right:
                                self.delete(self.root,temp)
                            else:
                                minimumParent.left = None
                            parent.data = temp
                            break
                    #1 child
                    elif check_node.left or check_node.right:
                        #if delete root
                        if parent is None:
                            if check_node.right:
                                check_node = check_node.right
                                next_node  = check_node
                            elif check_node.left:
                                check_node = check_node.left
                                next_node = check_node
                            self.root = next_node
                            break
                        else:
                            minimumParent = None
                            if check_node.right:
                                parent = check_node
                                check_node = check_node.right
                            elif check_node.left:
                                parent = check_node
                                check_node = check_node.left
                            while check_node.left:
                                minimumParent = check_node
                                check_node = check_node.left
                            parent.data = check_node.data
                            if minimumParent:
                                if minimumParent.right:
                                    minimumParent.left = None
                            else:
                                parent.right = None
                            break
                else:
                    print(f'Error! Not Found DATA')

        return self.root


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