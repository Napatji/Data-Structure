def straightSort(numlist, index):
    if index > -1:
        if checkSort(numlist) != True:
            if numlist[index] != checkMost(numlist,index):
                temp = numlist[index]
                most = checkMost(numlist,index)
                numlist[numlist.index(most)] = temp
                numlist[index] = most
                print(f'swap {temp} <-> {most} : {numlist}')
            return straightSort(numlist,index-1)
    return print(numlist)

#Check if list sorted or not
def checkSort(numlist,index = 0,checknum = 0):
    if index < len(numlist) - 1:
        if numlist[index] > numlist[index+1]:
            return False
        elif numlist[index] < numlist[index+1]:
            checknum = numlist[index+1]
            return checkSort(numlist,index+1,checknum)
    return True

#Find most value in list
def checkMost(numlist,index,maxnum=0):
    if index > -1:
        if maxnum < numlist[index]:
            maxnum = numlist[index]
        return checkMost(numlist,index-1,maxnum)
    return maxnum

if __name__ == '__main__':
    inp = input('Enter Input : ').split(' ')
    inp = list(map(int,inp))
    maxIndex = len(inp)-1
    straightSort(inp,maxIndex)