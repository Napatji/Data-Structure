def bubbleSort(numlist):
    temp = None
    if checkSort(numlist) is True:
        return print(f'last step : {numlist} move[{temp}]')
    else:
        step = 0
        for i in range(len(numlist)):
            step += 1       
            temp = numlist.pop(getMove(numlist))
            if temp < getMost(numlist):
                for i in numlist:
                    if i > temp:
                        numlist.insert(numlist.index(i),temp)
                        break
            else:
                numlist.append(temp)
            if checkSort(numlist) == False:
                print(f'{step} step : {numlist} move[{temp}]')    
            if checkSort(numlist) == True:
                print(f'last step : {numlist} move[{temp}]')
                break

def checkSort(numlist):
    check = True
    for i in range(0,len(numlist)-1):
        if int(numlist[i]) > int(numlist[i+1]):
            check = False
    return check

def getMove(numlist):
    check = True
    for i in range(len(numlist)):
        move = int(numlist[i])
        for j in range(i+1,len(numlist)):
            if move > numlist[j]:
                check = False
        if check == False:
            return i
    return None

def getMost(numlist):
    most = int(numlist[0])
    for i in numlist:
        if most < int(i):
            most = int(i)
    return most

def getLeast(numlist):
    least = int(numlist[0])
    for i in numlist:
        if least > int(i):
            least = int(i)
    return least

if __name__ == "__main__":
    inp = input('Enter Input : ').split(' ')
    inp = list(map(int,inp))
    bubbleSort(inp)