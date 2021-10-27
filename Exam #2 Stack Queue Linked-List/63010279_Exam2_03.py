class Queue:
    def __init__(self):
        self.queue =[]
    def enQueue(self, item):
        self.queue.append(item)
    def deQueue(self):
        if len(self.queue) > 0:
            return self.queue.pop(len(self.queue)-1)
    def isEmpty(self):
        if len(self.queue) > 0:
            return False
        else:
            return True
    def __len__(self):
        return len(self.queue)
    def __str__(self):
        value_left = ""
        if len(self.queue) > 0:
            for i in self.queue:
                value_left = value_left + str(i) + " "
            return "Queue data : {}".format(value_left)
        else:
            return ("Empty Queue")

class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data
    
    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.head
        for j in range(i) :
            p = p.next
        return p
    
    def reverse(self):
        temp=LinkedList()
        i = len(self)-1
        while i != -1:
            temp.append(self.nodeAt(i))
            i=i-1
        self.head=temp.head
            
if __name__ == "__main__":
    ll = LinkedList()
    inp = input("Enter numbers : ").split(' ')
    for i in inp:
        ll.append(i)
    print("Linkedlist Before Reverse")
    print(ll)
    print("Linkedlist After Reverse")
    ll.reverse()
    print(ll)
