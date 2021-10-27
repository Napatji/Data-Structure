class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value)
        while cur.next != None:
            s += " <- " + str(cur.next.value)
            cur = cur.next
        return s
    def isEmpty(self):
        if self.head == None:
            return True
        return False
    def append(self, item):
        if self.size == 0:
            new_node = Node(item)
            self.head = new_node
        else:
            new_node = Node(item)
            check_node = self.head
            while check_node.next:
                check_node = check_node.next
            check_node.next = new_node
        self.size += 1
    def addHead(self, item):
        if self.size == 0:
            new_node = Node(item)
            self.head = new_node
        else:
            new_node = Node(item)
            new_node.next = self.head
            self.head = new_node
        self.size += 1
    def search(self, item):
        check_node = self.head
        while check_node != None:
            if check_node.value == item:
                return "Found"
            check_node = check_node.next
        return "Not Found"
    def index(self, item):
        check_node = self.head
        index = 0
        while check_node != None:
            if check_node.value == item:
                return index
            index += 1
            check_node = check_node.next
        return -1
    def size(self):
        list_size = 0
        check_node = self.head
        while check_node != None:
            list_size += 1
            check_node = check_node.next
        return list_size
    def pop(self, pos):
        position = pos
        if self.head == None:
            return "Out of Range"
        else:
            if pos == 0:
                self.head = self.head.next
                return "Success"
            elif pos > 0 and pos < self.size:
                check_node = self.head
                prev_node = None
                for i in range(0,position):
                    prev_node = check_node
                    check_node = check_node.next
                prev_node.next = check_node.next
                return "Success"
            else:
                return "Out of Range"
    def sortList(self,list):
        queue = []
        use = list
        check_node = ""
        for i in list:
            if i != 0:
                queue.append(i)
            else :
                break
        for i in range(0,len(queue)):
            use.pop(0)
        for i in queue:
            use.append(i)
        for i in range(0,len(use)):
            newNode = Node(use[i])
            if i == 0:
                self.head = newNode
                check_node = self.head
            else:
                check_node.next = newNode
                check_node = check_node.next     

if __name__ == "__main__":
    print(" *** Re order ***")
    inp = input("Enter Input : ").split(' ')
    numlist = []
    link = LinkedList()
    for i in inp:
        numlist.append(int(i))
        link.append(i)
    print("Before : {}".format(link))
    link.sortList(numlist)
    print("After : {}".format(link))
