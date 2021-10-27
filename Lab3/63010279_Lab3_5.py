class Stack:
    def __init__(self):
        self.stack = list()
    def push(self, value):
        self.stack.append(value)
    def kritsadaLookback(self):
        if len(self.stack) == 0:
            print(len(self.stack))
        else:
            ref = self.stack[len(self.stack) - 1]
            see = 1
            #print(self.stack[::-1])
            for i in self.stack[::-1]:
                if i == ref:
                    ref = i
                    see += 0
                elif i > ref:
                    ref = i
                    see += 1
                else:
                    pass
            print(see)
    def kritsadaInfected(self):
        new = []
        for i in self.stack:
            if i % 2 ==0:
                if i - 1 >= 1:
                    i -= 1
                    new.append(i)
                else:
                    i = 1
                    new.append(i)
            else:
                i += 2
                new.append(i)
        #print(self.stack)
        self.stack = new
        #print(self.stack)      
                
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    input_num = []
    input_num = input('Enter Input : ').split(',')
    for ele in input_num:
        if ele[0] == "A":
            stack.push(int(ele[2:]))
        elif ele[0] == "B":
            stack.kritsadaLookback()
        elif ele[0] == "S":
            stack.kritsadaInfected()
        else:
            print("Error, please try again.")
