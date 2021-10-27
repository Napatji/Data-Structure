class Stack:
    def __init__(self):
        self.value = list()
    def __str__(self):
        display = ""
        if len(self.value) == 0:
            display = "Empty"
        else:
            for data in self.value:
                display = display + str(data) + " "
        return "Data in Stack is : {}".format(display) 
    def push(self,data):
        self.value.append(data)
    def pop(self):
        if len(self.value) > 0:
            self.value.pop()
    def isEmpty(self):
        if len(self.value) == 0:
            return True
        else:
            return False
    def size(self):
        return len(self.value)
    def peek(self):
        if len(self.value) > 0:
            return self.value[len(self.value) - 1]
        else:
            return None
    def bottom(self):
        if len(self.value) > 0:
            return self.value[0]
        else:
            return None
    
if __name__ == "__main__":
    user_input = input("Enter choice : ")
    if user_input == "1":
        s1 = Stack()
        s1.push(10)
        s1.push(20)
        print(s1)
        s1.pop()
        s1.push(30)
        print("Peek of stack :",s1.peek())
        print("Bottom of stack :",s1.bottom())
    if user_input == "2":
        s1 = Stack()
        s1.push(100)
        s1.push(200)
        s1.push(300)
        s1.pop()
        print(s1)
        print("Stack is Empty :",s1.isEmpty())
    if user_input == "3":
        s1 = Stack()
        s1.push(11)
        s1.push(22)
        s1.push(33)
        s1.pop()
        print(s1)
        print("Stack size :",s1.size())