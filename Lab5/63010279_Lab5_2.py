class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.index = 0

    def __str__(self):
        check_node = self.head
        if check_node == None:
            return ""
        else:
            current_data = str(self.head.value)
            if self.size == 1:
                return current_data
            else:
                while check_node.next:
                    current_data += "->" + str(check_node.next.value)
                    check_node = check_node.next
                return current_data

    def str_reverse(self):
        check_node = self.head
        if check_node == None:
            return ""
        else: 
            while check_node.next:
                check_node = check_node.next
            current_data = str(check_node.value)
            if self.size == 1:
                return current_data
            else:
                while check_node.previous:
                    current_data += "->" + str(check_node.previous.value)
                    check_node = check_node.previous
                return current_data

    def isEmpty(self):
        if self.head == None:
            return True
        else:
            return False

    def append(self, data): 
        if self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.head.previous = None
        else:
            new_node = Node(data)
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.previous = cur_node
        self.size += 1

    def insert(self, ind, data):
        index = ind
        check_node = self.head
        prev_node = None
        if index < 0 or index > self.size + 1:
            return ("Data cannot be added")
        elif index > 0 and index > self.size:
            return ("Data cannot be added")
        elif self.head == None:
            new_node = Node(data)
            self.head = new_node
            self.size += 1
            return ("index = {0} and data = {1}".format(index, data))
        else:
            new_node = Node(data)
            if index == 0:
                self.head.previous = new_node
                new_node.next = self.head
                new_node.previous = None
                self.head = new_node
                self.size += 1
                return ("index = {0} and data = {1}".format(index, data))
            elif index > 0:
                if index < self.size:
                    for i in range(0,index):
                        prev_node = check_node
                        check_node = check_node.next
                    prev_node.next = new_node
                    new_node.next = check_node
                    check_node.previous = new_node
                    new_node.previous = prev_node
                    self.size += 1
                    return ("index = {0} and data = {1}".format(index, data))
                elif index == self.size:
                    cur_node = self.head
                    while cur_node.next:
                        cur_node = cur_node.next
                    cur_node.next = new_node
                    new_node.previous = cur_node
                    self.size += 1
                    return ("index = {0} and data = {1}".format(index, data))
                elif index > self.size:
                    return ("index = {0} and data = {1}".format(index, data))

        self.size += 1

    def remove(self, data):
        check_node = self.head
        prev_node = None
        next_node = None
        index = 0
        if self.size == 0:
            return "Not Found!"
        else:
            if self.size == 1:
                self.head = None
                self.size -= 1
                self.index = index
                return
            else:
                check_node = self.head
                while check_node.value != data:
                    prev_node = check_node
                    check_node = check_node.next
                    index += 1
                if index == 0: #กรณี remove indexที่ 0
                    prev_node = check_node
                    check_node = check_node.next
                    prev_node.next = None
                    check_node.previous = None
                    self.head = check_node
                else:
                    next_node = check_node.next
                    prev_node.next = next_node
                    next_node.previous = prev_node
                    check_node.next = None
                    check_node.previous = None
                self.size -= 1
                self.index = index

if __name__ == "__main__":
    dlink = LinkedList()
    data = input("Enter Input : ").split(',')
    user_input = []
    for i in data:
        i = i.split(' ')
        if i[0] == '':
            i.pop(0)
        user_input.append(i)
    for i in user_input:
        if i[0] == "A":
            dlink.append(i[1])
        elif i[0] == "Ab":
            dlink.insert(0 ,i[1])
        elif i[0] == "I":
            j = i[1].split(':')
            index = int(j[0])
            data = int(j[1])
            print(dlink.insert(index, data))
        elif i[0] == "R":
            if(dlink.remove(i[1])) == "Not Found!":
                print("Not Found!")
            else:
                print("removed : {0} from index : {1}".format(i[1], dlink.index))
        print("linked list : {}".format(dlink))
        print("reverse : {}".format(dlink.str_reverse()))