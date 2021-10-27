class Queue:
    def __init__(self):
        self.value =[]
    def queue(self, item):
        self.value.append(item)
    def dequeue(self):
        if len(self.value) > 0:
            self.value.pop(0)
        else:
            print("Queue is empty.")
    def checkDuplicate(self):
        ref = set(self.value) #สร้าง Reference ของ Queue list
        if len(self.value) == len(ref):
            print("NO Duplicate")
        else:
            print("Duplicate")
    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    book = Queue()
    data = input("Enter Input : ").split('/',1)
    data_right = data[1].split(',')
    data_left = data[0].split()
    for i in range(0,len(data_left)):
        book.queue(data_left[i])
    for i in data_right:
        if i[0] == "E":
            book.queue(i[2:])
        elif i[0] == "D":
            book.dequeue()
        else:
            print("Error no command '{}' in program.".format(i[0]))
            break
    book.checkDuplicate()