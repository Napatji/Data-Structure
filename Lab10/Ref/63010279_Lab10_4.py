class hashtable():
    def __init__(self,size,MaxCollision,Threshold):
        self.size=size
        self.MaxCollision=MaxCollision
        self.Threshold=Threshold
        self.dataSize=0
        self.table=[]
        self.added=[]
        for _ in range(10000):
            self.table.append(None)
    def __str__(self):
        s=""
        for i in range(self.size):
            s=s+"#"+str(i+1)+"\t"+str(self.table[i])+"\n"
        return s[:-1]
    def thresholdCheck(self,data):
        if float(self.dataSize+1)/float(self.size)*100>self.Threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash()
    def add(self,data,re=False):
        self.thresholdCheck(data)
        index=data
        collisiontime=0
        oindex=index
        index=index%self.size
        while (self.table[index] is not None):
            collisiontime+=1
            print("collision number {} at {}".format(collisiontime,index))
            if collisiontime==self.MaxCollision:
                if re==False:
                    print("****** Max collision - Rehash !!! ******")
                self.rehash()
                collisiontime=0
            index=oindex+collisiontime*collisiontime
            index=index%self.size
        self.table[index]=data
        if re==False:
            self.added.append(data)
            self.dataSize+=1
    def rehash(self):
        self.size=self.size*2
        while not self.isPrime(self.size):
            self.size+=1
        self.table=[]
        for _ in range(10000):
            self.table.append(None)
        for i in self.added:
            self.add(i,True)
    def isPrime(self,num):
        for i in range(num-2):
            if num%(i+2)==0:
                return False
        return True       
print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")
size,MaxCollision,Threshold=inp[0].split(" ")
size = int(size)
MaxCollision = int(MaxCollision)
Threshold = int(Threshold)
t = hashtable(size,MaxCollision,Threshold)
print("Initial Table :")
print(t)
print("----------------------------------------")
add=[]
for i in inp[1].split(" "):
    add.append(int(i))
for i in add:
    print("Add : {}".format(i))
    t.add(i)
    print(t)
    print("----------------------------------------")