def move(n, source, helper, target,maxn):
    if n > 0:
        move(n - 1, source, target, helper,maxn)
        if source[0]:
            disk = source[0].pop()
            target[0].append(disk)
            print("move " + str(disk) + " from  " + source[1] + " to " + target[1])
            output(disk,source,target,helper,maxn)
        move(n - 1, helper, source, target,maxn)
def output(disk,source,target,helper,maxn):
    # Output
    templist=[]
    if source[1]== "A":
        t=source[0]
        templist.append(t)
    elif target[1]=="A":
        t=target[0]
        templist.append(t)
    elif helper[1]=="A":
        t=helper[0]
        templist.append(t)
    if source[1]== "B":
        t=source[0]
        templist.append(t)
    elif target[1]=="B":
        t=target[0]
        templist.append(t)
    elif helper[1]=="B":
        t=helper[0]
        templist.append(t)
    if source[1]== "C":
        t=source[0]
        templist.append(t)
    elif target[1]=="C":
        t=target[0]
        templist.append(t)
    elif helper[1]=="C":
        t=helper[0]
        templist.append(t)
    forReplace(templist,maxn)
    # Output
def forReplace(templist,i):
        if i+1>len(templist[0]):
            print ("|",end="  ")
        else:
            print (templist[0][i],end="  ")
        if i+1>len(templist[1]):
            print ("|",end="  ")
        else:
            print (templist[1][i],end="  ")
        if i+1>len(templist[2]):
            print ("|",end="  ")
        else:
            print (templist[2][i],end="  ")
        print("")
        if i==0:
            return
        else:
            return forReplace(templist,i-1)
def inputAppend(source,n,i):
    source[0].append(n-i)
    if i < n-1:
        return inputAppend(source,n,i+1)
    else:
        return
if __name__=="__main__":
    n = int(input("Enter Input : "))
    source = ([], "A")
    target = ([], "C")
    helper = ([], "B")
    inputAppend(source,n,0)
    output(n,source,helper,target,n+1)
    move(n,source,helper,target,n+1) 