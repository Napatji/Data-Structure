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
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
        self.size += 1

    def addHead(self, item):
        new_head = Node(item)
        new_head.next = self.head
        self.head = new_head
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
        while check_node:
            if check_node.value == item:
                return index
            index += 1
            check_node = check_node.next
        return -1

    def size(self):
        count = 0
        for i in range(0,int(self.size)):
            count += 1
        return count

    def pop(self, position):
        self.size -= 1
        check_node = self.head #index[0]
        prev_node = None #set Previous Node
        if position > self.size - 1 or position < 0:
            return "Out of Range"
        else:
            if position == 0:
                self.head = check_node.next
                check_node = None
            else:
                for i in range(0,position+1):
                    if i > 0:
                        prev_node = check_node
                        check_node = check_node.next
                prev_node.next = check_node.next
                check_node = None
            return "Success"
    
if __name__ == "__main__":
    L = LinkedList()
    inp = input('Enter Input : ').split(',')
    for i in inp:
        if i[:2] == "AP":
            L.append(i[3:])
        elif i[:2] == "AH":
            L.addHead(i[3:])
        elif i[:2] == "SE":
            print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
        elif i[:2] == "SI":
            print("Linked List size = {0} : {1}".format(L.size, L))
        elif i[:2] == "ID":
            print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
        elif i[:2] == "PO":
            before = "{}".format(L)
            k = L.pop(int(i[3:]))
            print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    print("Linked List :", L)