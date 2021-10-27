class Stack() :
    def __init__(self):
        self.stack = list()
    def push(self, item):
        self.stack.append(item)
        print("Add = {} and Size = {}".format(item,len(self.stack)))
    def pop(self):
        if len(self.stack) == 0:
            print("-1")
        elif len(self.stack) > 0:
            print("Pop = {} and Index = {}".format(self.stack[-1],len(self.stack)-1))
            self.stack.pop()
    def peek(self):
        if len(self.stack) > 0:
            return self.stack[len(self.stack) - 1]
        else:
            return None
    def __str__(self):
        output = ""
        if len(self.stack) == 0:
            output = "Empty"
        else:
            for number in self.stack:
                output = output + str(number) +" "
        return ("Value in Stack = {}".format(output))

if __name__ == "__main__":
    stack = Stack()
    input_num = []
    input_num = input("Enter Input : ").split(',')
    for ele in input_num:
        if ele[0] == "A":
            stack.push(int(ele[2:]))
        elif ele[0] == "P":
            stack.pop()
        else:
            print("Error, please try again.")
    print(stack)