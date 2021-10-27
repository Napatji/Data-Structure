class node():
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class linklist():
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
        else:
            self.tail.next=newnode
        self.tail=newnode
    def __str__(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" "+str(last.next.data)
            last=last.next
        return temp
    def isEmpty(self):
        if self.head is None:
            return True
        else:
            return False
    def dequeue(self):
        temp=self.head.data
        self.head=self.head.next
        return temp
    def size(self):
        size=0
        last=self.head
        while last is not None:
            last=last.next
            size=size+1
        return  size
    def sort(self):
        for i in range(self.size()-1):
            last=self.head
            while last.next is not None:
                if last.data>last.next.data:
                    temp=last.data
                    last.data=last.next.data
                    last.next.data=temp
                last=last.next
    def result(self):
        if self.head is None:
            return ""
        temp=str(self.head.data)
        last=self.head
        while (last.next is not None):
            temp=temp+" -> "+str(last.next.data)
            last=last.next
        return temp

if __name__=="__main__":
    inp=input("Enter Input : ").split()
    ll=linklist()
    lloriginal=linklist()
    for i in inp:
        ll.append(i)
        lloriginal.append(i)
    ll0=linklist()
    ll1=linklist()
    ll2=linklist()
    ll3=linklist()
    ll4=linklist()
    ll5=linklist()
    ll6=linklist()
    ll7=linklist()
    ll8=linklist()
    ll9=linklist()
    divider=1
    round=1
    while not ll.isEmpty():
        value=int(ll.dequeue())
        if value<0:
            temp=(0-value)%10
        else:
            temp=value%10
        if temp==0:
            ll0.append(value)
        elif temp==1:
            ll1.append(value)
        elif temp==2:
            ll2.append(value)
        elif temp==3:
            ll3.append(value)
        elif temp==4:
            ll4.append(value)
        elif temp==5:
            ll5.append(value)
        elif temp==6:
            ll6.append(value)
        elif temp==7:
            ll7.append(value)
        elif temp==8:
            ll8.append(value)
        elif temp==9:
            ll9.append(value)
    ll0.sort()
    ll1.sort()
    ll2.sort()
    ll3.sort()
    ll4.sort()
    ll5.sort()
    ll6.sort()
    ll7.sort()
    ll8.sort()
    ll9.sort()
    while (True):
        print("------------------------------------------------------------")
        print("Round : {}".format(round))
        print("0 :",ll0)
        print("1 :",ll1)
        print("2 :",ll2)
        print("3 :",ll3)
        print("4 :",ll4)
        print("5 :",ll5)
        print("6 :",ll6)
        print("7 :",ll7)
        print("8 :",ll8)
        print("9 :",ll9)
        if(ll1.isEmpty() and ll2.isEmpty() and ll3.isEmpty() and ll4.isEmpty() and ll5.isEmpty() and ll6.isEmpty() and ll7.isEmpty() and ll8.isEmpty() and ll9.isEmpty()):
            break
        ######################################################################
        round=round+1
        divider=divider*10
        newll0=linklist()
        newll1=linklist()
        newll2=linklist()
        newll3=linklist()
        newll4=linklist()
        newll5=linklist()
        newll6=linklist()
        newll7=linklist()
        newll8=linklist()
        newll9=linklist()
        #
        while not ll0.isEmpty():
            value=int(ll0.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll1.isEmpty():
            value=int(ll1.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll2.isEmpty():
            value=int(ll2.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll3.isEmpty():
            value=int(ll3.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll4.isEmpty():
            value=int(ll4.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll5.isEmpty():
            value=int(ll5.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll6.isEmpty():
            value=int(ll6.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll7.isEmpty():
            value=int(ll7.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll8.isEmpty():
            value=int(ll8.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        while not ll9.isEmpty():
            value=int(ll9.dequeue())
            if value<0:
                temp=(0-int(value/divider))%10
            else:
                temp=int(value/divider)%10
            if temp==0:
                newll0.append(value)
            elif temp==1:
                newll1.append(value)
            elif temp==2:
                newll2.append(value)
            elif temp==3:
                newll3.append(value)
            elif temp==4:
                newll4.append(value)
            elif temp==5:
                newll5.append(value)
            elif temp==6:
                newll6.append(value)
            elif temp==7:
                newll7.append(value)
            elif temp==8:
                newll8.append(value)
            elif temp==9:
                newll9.append(value)
        ll0=newll0
        ll1=newll1
        ll2=newll2
        ll3=newll3
        ll4=newll4
        ll5=newll5
        ll6=newll6
        ll7=newll7
        ll8=newll8
        ll9=newll9
        ll0.sort()
        ll1.sort()
        ll2.sort()
        ll3.sort()
        ll4.sort()
        ll5.sort()
        ll6.sort()
        ll7.sort()
        ll8.sort()
        ll9.sort()
    print("------------------------------------------------------------")
    print("{} Time(s)".format(round-1))
    print("Before Radix Sort : ",end="")
    print(lloriginal.result())
    print("After  Radix Sort : ",end="")
    print(ll0.result())
