class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self,size,maxColli):
        self.size =size
        self.maxColli=maxColli
        self.table=[]
        for i in range(size):
            self.table.append(None)
    def __str__(self):
        s=""
        for i in range(len(self.table)):
            s=s+"#"+str(i+1)+"      "+str(self.table[i])+"\n"
        return s
    def insert(self,key,value):
        #key
        originalkeySum=0
        for i in key:
            originalkeySum+=ord(i)
        colliCounter=0
        keySum=originalkeySum
        while True:
            if colliCounter==self.maxColli:
                print("Max of collisionChain")
                return
            if self.table[keySum%self.size] is not None:
                colliCounter+=1
                print("collision number {} at {}".format(colliCounter,(keySum%self.size)))
                keySum=originalkeySum+colliCounter*colliCounter
            else:
                self.table[keySum%self.size]=Data(key,value)
                break
    def isFull(self):
        c=0
        for i in self.table:
            if i is not None:
                c+=1
        return c==self.size
if __name__=="__main__":
    print(" ***** Fun with hashing *****")
    inp =input("Enter Input : ").split("/")
    size,maxColli=inp[0].split(" ")
    size=int(size)
    maxColli=int(maxColli)
    inp[1]=inp[1].split(",")
    h=hash(size,maxColli)
    for i in inp[1]:
        if (h.isFull()):
            print("This table is full !!!!!!")
            break
        key,value=i.split(" ")
        h.insert(key,value)
        print(h,end="")
        print("---------------------------")