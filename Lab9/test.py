def bubbleSort(numlist):
    if checkSort(numlist) is True:
        return print(f'last step : {numlist} move[None]')
    else:
        step = 0
        list_left = None
        for i in numlist:
            if i == getLeast(numlist):
                if numlist.index(i) != len(numlist)-1:
                    list_left = numlist[step+1:len(numlist)+1]
                break
            step += 1
        if list_left != None:
            step = 0
            for i in range(getLeast(numlist),getLeast(list_left)-1):
                step += 1
        for i in range(step):
            most = True
            if checkSort(numlist) == False:
                temp = numlist.pop(0)  
            else:
                temp = None
            if temp!= None:
                for j in range(len(numlist)):
                    if numlist[j] > temp:
                        most = False
                    if temp < numlist[j]:
                        numlist.insert(j,temp)
                        break
                if most == True:
                    numlist.append(temp)
            if i == step-1:
                print(f'last step : {numlist} move[{temp}]')
            else:
                print(f'{i+1} step : {numlist} move[{temp}]')

def checkSort(numlist):
    check = True
    for i in range(0,len(numlist)-1):
        if int(numlist[i]) > int(numlist[i+1]):
            check = False
    return check

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