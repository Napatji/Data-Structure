def sortSubset(numlist):
    pass

def generateSubset(numlist):
    subset = []
    temp = []
    for i in numlist:
        temp.append(i)
    # j = ตัวเลขตัวแรก
    for i in range(0,len(numlist)):    
        for j in range(1,len(numlist)+1):
            if j == 1:
                subset.append([numlist[i]])
            elif j == 2:
                if numlist[i] != numlist[j-1]:
                    subset.append([numlist[i],numlist[j-1]])
            else:
                subset.append(numlist[i:j])
    print(subset)

def getSum(subset):
    result = 0
    for i in subset:
        result += int(i)
    return result

def sortNum(numlist):
    temp = []
    while True:
        if len(numlist) != 0:
            least = getLeast(numlist)
            temp.append(least)
            numlist.pop(numlist.index(least))
        else:
            break
    return temp

def isSort(numlist):
    check = True
    for i in range(len(numlist)-1):
        if numlist[i] > numlist[i+1]:
            check = False
    return check

def getLeast(numlist):
    least = numlist[0]
    for i in range(0,len(numlist)-1):
        if least > numlist[i+1]:
            least = numlist[i+1]
    return least

def compare(subset):
    pass

if __name__ == '__main__':
    result,numlist = input('Enter Input : ').split('/')
    numlist = numlist.split(' ')
    numlist = list(map(int,numlist))
    generateSubset([1,2,3])