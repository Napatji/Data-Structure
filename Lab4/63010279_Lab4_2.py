class Queue:
    def __init__(self):
        self.value =[]
    def queue(self, item):
        self.value.append(item)
    def dequeue(self):
        if len(self.value) > 0:
            self.value.pop(0)
    def setSize(self,size): #กำหนดขนาด
        self.size = size
    def isFull(self): #ตรวจสอบว่าเต็มหรือยัง
        if len(self.value) == self.size:
            return True
        else:
            return False
    def __str__(self):
        return str(self.value)

if __name__ == "__main__":
    main = Queue()
    cashier1 = Queue()
    cashier2 = Queue()
    cashier1.setSize(5)
    cashier2.setSize(5)
    data_in = []
    data_in = input("Enter people and time : ").split()
    row = int(data_in[1]) # กำหนดแถว
    for i in data_in[0]: # queue input in MainQueue.
        main.queue(i)
    c1 = False #เช็คว่ามีคนในแถว 1 มั้ย
    c2 = False #เช็คว่ามีคนในแถว 2 มั้ย
    cashier1_count = 0 # นับนาทีแถว 1
    cashier2_count = 0 # นับนาทีแถว 2
    for i in range(0,row): # จัดการแถว
        main.dequeue()
        if cashier1.isFull() == False and i+1 <= len(data_in[0]):
            cashier1.queue(data_in[0][0+i])
            c1 = True
        elif cashier1.isFull() == True and i+1 <= len(data_in[0]):
            if cashier2.isFull() == False:
                cashier2.queue(data_in[0][0+i])      
                c2 = True
        print(i+1,main,cashier1,cashier2) # เวลาและแสดงแถว
        if c1 == True:
            cashier1_count += 1 
        if c2 == True:
            cashier2_count += 1
        if cashier1_count % 3 == 0:
            cashier1.dequeue()
        if cashier2_count % 2 == 0:
            cashier2.dequeue()