class Queue:
    def __init__(self):
        self.value = []
    def enQueue(self, item):
        if len(self.value) <= 1:
            self.value.append(item)
        else:
            for i in range(len(self.value) - 1, -1, -1):
                if item[0] == self.value[i][0]:
                    self.value.insert(i+1, item)
                    break
            else:
                self.value.append(item)
    def deQueue(self):
        return self.value.pop(0)[1]
    def isEmpty(self):
        return self.value == []
    def size(self):
        return len(self.value)

def getID(lists, code):
    for item in lists:
        if code == item[1]:
            return item[0]

if __name__ == "__main__":
    queue = Queue()
    stackQueue = Queue()
    data = input("Enter Input : ").split("/")
    employees = data[0]
    orders = data[1]
    employees = [x.split() for x in employees.split(",")]
    orders = [x.split() for x in orders.split(",")]

    for order in orders:
        if order[0] == "E":
            code = getID(employees, order[1])
            queue.enQueue([code, order[1]])
        elif order[0] == "D":
            if queue.isEmpty():
                print("Empty")
            else:
                print(queue.deQueue())