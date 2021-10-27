class Stack:
    def __init__(self):
        self.value=[]
        self.score={'+':1, '-':1, '*':2, '/':2, '^':3, '(':0}
    def push(self, value):
        self.value.append(value)
    def pop(self):
        temp=self.value[-1]
        self.value.pop()
        return temp
    def size(self):
        return len(self.value)
    def isEmpty(self):
        if len(self.value)==0:
            return 1
        else:
            return 0
    def peek(self):
        return self.value[-1]
    def reverse(self):
        temp=[]
        for i in reversed(self.value):
            temp.append(i)
        self.value=temp

inp = input('Enter Infix : ')

S = Stack()

print('Postfix : ', end='')
temp = Stack()
for i in inp:
    if i not in '+-*/^()':
        S.push(i)
    elif i in '(':
        temp.push(i)
    elif i in ')':
        while (temp.peek()!="(" and not temp.isEmpty()):
            S.push(temp.pop())
        if (temp.peek()=='('):
            temp.pop()
    else:
        while(not temp.isEmpty() and temp.score[i]<=temp.score[temp.peek()]):
            S.push(temp.pop())
        temp.push(i)

while not temp.isEmpty():
    S.push(temp.pop())
S.reverse()


while not S.isEmpty():

    print(S.pop(), end='')

print()