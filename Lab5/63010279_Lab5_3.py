class Node:
    def __init__(self, data):
        self.value = data
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

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
                    current_data += " " + str(check_node.next.value)  
                    check_node = check_node.next
                return current_data

    def reverse(self):
        check_node = self.head
        if check_node == None:
            return ""
        else: 
            while check_node.next:
                check_node = check_node.next
            current_data = str(check_node.value) + " "
            if self.size == 1:
                return current_data
            else:
                while check_node.previous:
                    current_data += str(check_node.previous.value) + " "
                    check_node = check_node.previous
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

def merge(linkedlist1, linkedlist2):
    merge_list = LinkedList()
    l1 = str(linkedlist1).split('->')
    l2 = str(linkedlist2).split('->')
    for i in l1:
        merge_list.append(i)
    for i in l2:
        merge_list.append(i)
    return merge_list
    

if __name__ == "__main__":
    inp = input("Enter Input (L1,L2) : ").split()
    l1 = inp[0].split('->')
    l2 = inp[1].split('->')
    L1 = LinkedList()
    L2 = LinkedList()
    for i in l1:
        L1.append(i)  
    for i in l2:
        L2.append(i) 
    print("L1    : {}".format(L1))
    print("L2    : {}".format(L2))
    print("Merge : {}".format(merge(L1,L2.reverse())))