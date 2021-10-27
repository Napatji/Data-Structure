class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None

class Linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        check_node = self.head
        if check_node == None:
            return "Empty"
        else:
            current_data = str(self.head.value)
            if self.size == 1:
                return current_data
            else:
                while check_node.next:
                    current_data += "->" + str(check_node.next.value)
                    check_node = check_node.next
                return current_data
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.previous = None
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.previous = cur_node
        self.size += 1
    def setNext(self, index1, index2):
        if self.size == 0:
            print("Error! {list is empty}")
        elif index1 >= self.size or index1 < 0:
            print("Error! {index not in length}:",str(index1))
        else:
            if index2 >= self.size:
                new_node = Node(index2)
                cur_node = self.head
                while cur_node.next:
                    cur_node = cur_node.next
                cur_node.next = new_node
                new_node.previous = cur_node
                self.size += 1
                print("index not in length, append :", index2)
            elif index2 >= 0 and index2 < self.size:
                check_node1 = self.head
                check_node2 = self.head
                for i in range(0,index1):
                    check_node1 = check_node1.next
                for i in range(0,index2):
                    check_node2 = check_node2.next
                check_node1.next = check_node2
                check_node2.previous = check_node1
                print("Set node.next complete!, index:value = {0}:{1} -> {2}:{3}".format(index1, check_node1.value, index2, check_node2.value))
    def checkLoop(self):
        s = set()
        check = self.head
        while (check):
            if (check in s):
                return True
            s.add(check)
            check = check.next
        return False
    
if __name__ == "__main__":
    inp = input("Enter input : ").split(',')
    LL = Linkedlist()
    user_input = []
    for i in inp:
        user_input.append(i.split())
    for i in user_input:
        if i[0] == 'A':
            LL.append(i[1])
            print(LL)
        elif i[0] == 'S':
            data = i[1].split(':')
            i1 = int(data[0])
            i2 = int(data[1])
            LL.setNext(i1, i2)
    if LL.checkLoop() == True:
        print("Found Loop")
    elif LL.checkLoop() == False:
        print("No Loop")
        print(LL)

    