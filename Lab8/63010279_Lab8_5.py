class Node:
    def __init__(self, data, index = 1, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.index = index
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None
        self.maxIndex = 1

    def insert(self, root, data):#insert แบบ Complete BST
        if root is None:
            return Node(data, self.maxIndex)
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

    def checkChild(self, node):#Checkลูก
        if node.left and node.right:
            return True
        return False

    def findAlmostLeft(self, node):#หาNodeเกือบซ้าย
        find = node
        if not find.left.left:
            return node
        else:
            return self.findAlmostLeft(find.left)

    def findIndex(self, node, index):#หาIndex แล้วreturn Nodeที่Indexนั้นกลับมา
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

    def rent(self, node, day):#เพิ่มจำนวนวันที่เช่าลงใน Data
        node.data += day
        return node

    def findLeast(self, root):#หา Node ที่มีจำนวนวันที่เช่าน้อยที่สุด
        node = root
        for i in range(1,self.maxIndex+1):#Check ตั้งแต่ Indexแรก
            check = self.findIndex(root,i)
            if not check:
                break
            elif check.data < node.data:
                node = check
        return node

if __name__ == "__main__":
    tree = BST()
    root = None
    van_num,rent_day = input('Enter Input : ').split('/')
    van_num = list(map(int,van_num))
    rent_day = list(map(int,rent_day.split(' ')))
    #ประกาศรถตู้
    for i in range(1,van_num[0]+1):
        root = tree.insert(root,0)#เพิ่มวันที่เช่ารถตู้ทุกคันเป็น 0
    # จองรถตู้
    num = 1
    for i in rent_day:
        rent_van = tree.findLeast(root)
        rent_van = tree.rent(rent_van, i)
        print(f'Customer {num} Booking Van {rent_van.index} | {i} day(s)')
        num += 1