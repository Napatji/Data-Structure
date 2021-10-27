class Queue:
    def __init__(self):
        self.value =[]
    def enqueue(self, item):
        self.value.append(item)
    def dequeue(self):
        if len(self.value) > 0:
            self.value.pop(0)
    def __str__(self):
        if len(self.value) > 0:
            value_left = ""
            for i in self.value:
                value_left = value_left + i +  " "
            return str(value_left)
        else:
            return ("Empty")
    def checkDuplicate(self):
        if len(self.value) == len(set(self.value)):
            return "NO Duplicate"
        else:
            return "Duplicate"

if __name__ == "__main__":
    item = Queue()
    book,method = input("Enter Input : ").split('/')
    usebook = book.split(' ')
    usemethod = method.split(',')
    for i in usebook:
        item.enqueue(i)
    for i in usemethod:
        if i[0] == "E":
            item.enqueue(i[2:])
        if i[0] == "D":
            item.dequeue()
    print(item.checkDuplicate())
