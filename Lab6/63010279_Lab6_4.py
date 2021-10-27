def addObject(start,n,i):
    start[0].append(n-i)
    if i < n-1:
        return addObject(start,n,i+1)
    else:
        return

def display(objective,start,end,path,row):
    data=[]
    if start[1]== "A":
        t=start[0]
        data.append(t)
    elif end[1]=="A":
        t=end[0]
        data.append(t)
    elif path[1]=="A":
        t=path[0]
        data.append(t)
    if start[1]== "B":
        t=start[0]
        data.append(t)
    elif end[1]=="B":
        t=end[0]
        data.append(t)
    elif path[1]=="B":
        t=path[0]
        data.append(t)
    if start[1]== "C":
        t=start[0]
        data.append(t)
    elif end[1]=="C":
        t=end[0]
        data.append(t)
    elif path[1]=="C":
        t=path[0]
        data.append(t)
    sortDisplay(data,row)
    
def sortDisplay(data,i):
        if i+1>len(data[0]):
            print ("|",end="  ")
        else:
            print (data[0][i],end="  ")
        if i+1>len(data[1]):
            print ("|",end="  ")
        else:
            print (data[1][i],end="  ")
        if i+1>len(data[2]):
            print ("|",end="  ")
        else:
            print (data[2][i],end="  ")
        print("")
        if i==0:
            return
        else:
            return sortDisplay(data,i-1)

def move(n,start,path,end,maxn):
    if n > 0:
        move(n-1,start,end,path,maxn)
        if start[0]:
            objective = start[0].pop()
            end[0].append(objective)
            print("move {0} from  {1} to {2}".format(n, start[1], end[1]))
            display(objective,start,end,path,maxn - 1)
        move(n-1,path,start,end,maxn)

if __name__ == "__main__":
    n = int(input("Enter Input : "))
    start = ([], "A")
    path = ([], "B")
    end = ([], "C")
    addObject(start,n,0)
    display(n,start,path,end,n)
    move(n,start,path,end,n + 1)