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