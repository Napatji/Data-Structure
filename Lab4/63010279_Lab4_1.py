class Queue:
    def __init__(self):
        self.value =[]
    def queue(self, item):
        self.value.append(item)
        print(len(self.value))
    def dequeue(self):
        if len(self.value) > 0:
            print(str(self.value[0])+" 0")
            self.value.pop(0)
        else:
            print(-1)
    def __str__(self):
        if len(self.value) > 0:
            value_left = ""
            for i in self.value:
                value_left = value_left + i + " "
            return str(value_left)
        else:
            return ("Empty")

if __name__ == "__main__":
    Q = Queue()
    data_in = []
    data_in = input("Enter Input : ").split(',')
    for i in data_in:
        if i[0] == "E":
            Q.queue(i[2:])
        elif i[0] == "D":
            Q.dequeue()
    print(Q)