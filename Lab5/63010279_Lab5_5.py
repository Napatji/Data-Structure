class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

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
    def beforeORafter(self):
        check_node = self.head
        if check_node == None:
            return ""
        else:
            current_data = str(self.head.value)
            if self.size == 1:
                return current_data
            else:
                while check_node.next:
                    current_data += " -> " + str(check_node.next.value)
                    check_node = check_node.next
                return current_data
    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.size += 1
    def clear(self):
        while (self.head != None):
            temp = self.head
            self.head = self.head.next
            temp = None
        self.size = 0
    def sort(self):
        if self.size > 1:
            new_sort = []
            check_node = self.head
            new_sort.append(check_node.value)
            while check_node.next:
                check_node = check_node.next
                new_sort.append(check_node.value)
            new_sort.sort()
            new_node = self.head
            self.head = new_node
            for i in new_sort:
                new_node.value = i
                new_node= new_node.next                           
    def getMaxBit(self): #หาค่าจำนวนหลักที่มากที่สุด
        check_node = self.head
        maxbit = 0
        while check_node:
            i = 0
            while check_node.value > 0:
                check_node.value //= 10
                i += 1
            if i > maxbit:
                maxbit = i
            check_node = check_node.next
        return int(maxbit)

def getDigit(number, bit): #หาค่าหลัก
    if number >= 0:
        for i in range(bit - 1):
            number //= 10
        return number % 10
    else:
        number *= -1
        for i in range(bit - 1):
            number //= 10
        return number % 10

if __name__ == "__main__":
    user_input = input("Enter Input : ").split()
    LL = LinkedList()#print original
    LLsort = LinkedList()
    ref = LinkedList() #getMaxBit
    time = 0
    line0 = LinkedList()
    line1 = LinkedList()
    line2 = LinkedList()
    line3 = LinkedList()
    line4 = LinkedList()
    line5 = LinkedList()
    line6 = LinkedList()
    line7 = LinkedList()
    line8 = LinkedList()
    line9 = LinkedList()
    for i in user_input:
        LL.append(int(i))
        ref.append(int(i))
        LLsort.append(int(i))
    print("------------------------------------------------------------")
    for i in range(ref.getMaxBit() + 1):
        line0.clear()
        line1.clear() 
        line2.clear()
        line3.clear()
        line4.clear()
        line5.clear()
        line6.clear()
        line7.clear()
        line8.clear()
        line9.clear()
        for num in user_input:
            if getDigit(int(num), i+1) == 0:
                line0.append(int(num))
            elif getDigit(int(num), i+1) == 1:
                line1.append(int(num))
            elif getDigit(int(num), i+1) == 2:
                line2.append(int(num))
            elif getDigit(int(num), i+1) == 3:
                line3.append(int(num))
            elif getDigit(int(num), i+1) == 4:
                line4.append(int(num))
            elif getDigit(int(num), i+1) == 5:
                line5.append(int(num))
            elif getDigit(int(num), i+1) == 6:
                line6.append(int(num))
            elif getDigit(int(num), i+1) == 7:
                line7.append(int(num))
            elif getDigit(int(num), i+1) == 8:
                line8.append(int(num))
            elif getDigit(int(num), i+1) == 9:
                line9.append(int(num))
        line0.sort()
        line1.sort()
        line2.sort()
        line3.sort()
        line4.sort()
        line5.sort()
        line6.sort()
        line7.sort()
        line8.sort()
        line9.sort()
        print("Round : {}".format(i+1))
        print("0 : {}".format(line0))
        print("1 : {}".format(line1))
        print("2 : {}".format(line2))
        print("3 : {}".format(line3))
        print("4 : {}".format(line4))
        print("5 : {}".format(line5))
        print("6 : {}".format(line6))
        print("7 : {}".format(line7))
        print("8 : {}".format(line8))
        print("9 : {}".format(line9))
        print("------------------------------------------------------------")
        time = i
        if line0.size == LL.size:
            break
    print("{} Time(s)".format(time))
    print("Before Radix Sort : {}".format(LL.beforeORafter()))
    print("After  Radix Sort : {}".format(line0.beforeORafter()))