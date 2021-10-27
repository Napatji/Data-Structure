class Queue:
    def __init__(self, list=None):
        if list == None:
            self.items = []
        else:
            self.items = list
    def enqueue(self, i):
        self.items.append(i)
    def dequeue(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class Stack:
 def __init__(self, list = None):
    if list == None:        
     self.items = []    
    else:
     self.items= list
 def __str__(self):
    s = 'stack of'+str(self.size())+'items:'
    for ele in self.items:
         s += str(ele)+''
    return s        
 def push(self,i):
    self.items.append(i)    
 def pop(self):
    return self.items.pop()
 def peek(self):
    return self.items[-1]
 def isEmpty(self):
    return self.items == []     
 def size(self):
    return len(self.items)


n = input('Enter Input (Normal, Mirror) : ').split()
s = Stack()
mirror_Bomb = Queue()
mirror_Stack = Stack()
normal_Queue = Queue()
exp_Count =0
fail_Count =0
for e in n[1]:
    s.push(e)

while not s.isEmpty():    
    if s.size()>=3 and s.items[-1]==s.items[-2]==s.items[-3]:
        mirror_Bomb.enqueue(s.pop())
        s.pop()
        s.pop()
    else:
        mirror_Stack.push(s.pop())
    if mirror_Stack.size()>=3:
        if mirror_Stack.items[-1]==mirror_Stack.items[-2]==mirror_Stack.items[-3]:
            mirror_Bomb.enqueue(mirror_Stack.pop())
            mirror_Stack.pop()
            mirror_Stack.pop()

mirror_exp_Count = mirror_Bomb.size()
for e in n[0][::-1]:
    s.push(e)

while not s.isEmpty():
    if s.size()>=3 and s.items[-1]==s.items[-2]==s.items[-3]:
        if  not(mirror_Bomb.isEmpty()) and mirror_Bomb.items[0] != s.items[-1]:
            normal_Queue.enqueue(s.pop())
            normal_Queue.enqueue(s.pop())
            normal_Queue.enqueue(mirror_Bomb.dequeue())
            normal_Queue.enqueue(s.pop())        
        elif not(mirror_Bomb.isEmpty()) and mirror_Bomb.items[0] == s.items[-1]:
            normal_Queue.enqueue(s.pop())
            s.pop()
            mirror_Bomb.dequeue()
            s.pop()            
            fail_Count +=1            
        elif mirror_Bomb.isEmpty():
            s.pop()
            s.pop()
            s.pop()
            exp_Count+=1            
    else:
            normal_Queue.enqueue(s.pop())
    if normal_Queue.size()>=3:
        if normal_Queue.items[-1]== normal_Queue.items[-2]==normal_Queue.items[-3]:
            normal_Queue.items.pop()
            normal_Queue.items.pop()
            normal_Queue.items.pop()
            exp_Count +=1

print('NORMAL :')
print(normal_Queue.size())
if normal_Queue.size()==0:
    print('Empty')
else:
    for e in normal_Queue.items[::-1]:
        print(e,end='')
    print('')
print(f'{exp_Count} Explosive(s) ! ! ! (NORMAL)')
if(fail_Count!=0):
    print(f'Failed Interrupted {fail_Count} Bomb(s)')
print('------------MIRROR------------')
print(': RORRIM')
print(mirror_Stack.size())
if(mirror_Stack.size()==0):
    print('ytpmE')
else:
    for e in mirror_Stack.items[::-1]:
        print(e,end='')
    print('')
print(f'(RORRIM) ! ! ! (s)evisolpxE {mirror_exp_Count}')
