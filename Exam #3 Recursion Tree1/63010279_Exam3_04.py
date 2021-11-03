import math
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):  
        if self.root == None:
            self.root = TreeNode(val)
        else:
            check_node = self.root
            while True:
                if check_node.val < val:
                    if check_node.right:
                        check_node = check_node.right
                    else:
                        check_node.right = TreeNode(val)
                        break
                elif check_node.val >= val:
                    if check_node.left:
                        check_node = check_node.left
                    else:
                        check_node.left = TreeNode(val)
                        break
        return self.root

def midValue(list_nums):
    if len(list_nums) % 2 == 0:
        return len(list_nums)/2
    else:
        return math.floor(len(list_nums)/2)

def list_to_bst(list_nums):
    T = BST()
    mid = midValue(list_nums)
    root = T.insert(list_nums[mid])
    left = []
    right = []
    for i in range(0,mid):
        left.append(list_nums[i])
    for i in range(mid+1,len(list_nums)-1):
        right.append(list_nums[i])
    for i in right:
        root = T.insert(i)
    for i in left:
        root = T.insert(i)
    return root

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)   

def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)

if __name__ == "__main__":
    list_nums = sorted([int(item) for item in input("Enter list : ").split()])
    result = list_to_bst(list_nums)
    print("\nList to a height balanced BST : ")
    print(preOrder(result))
    print("\nBST model : ")
    printBST(result)