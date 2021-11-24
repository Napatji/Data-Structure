def insertion(numlist):
    step = 0
    temp = None
    if checkSort(numlist) is True:
        temp = numlist
        step += len(numlist) - 1
    else:
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
            if checkSort(numlist) == True:
                break
        step += len(numlist) - 1
    return step

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

if __name__ == '__main__':
    print(' *** Insertion sort ***')
    inp = input('Enter some numbers : ').split(' ')
    inp = list(map(int,inp))
    step = insertion(inp)
    print(' ')
    print(f'{inp}')
    print(f'Data comparison =  {step}')
    print(getMove([5, 6, 13, 26, 42, 1, 97, 53, 9, 73]))