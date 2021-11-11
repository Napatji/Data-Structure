def bubbleSort(numlist):
    count = 0
    temp = []
    display = []
    for i in numlist:
        display.append(int(i))
    while numlist:
        count += 1
        move = checkLeast(numlist)
        numlist.remove(str(move))
        temp.append(move)
        if len(numlist) == 1:
            pass
        else:
            # print(f'{count} step : {} move[4]')
            pass
    return temp

def checkLeast(numlist):
    least = int(numlist[0])
    for i in numlist:
        if least > int(i):
            least = int(i)
    return least

if __name__ == "__main__":
    inp = input('Enter Input : ').split(' ')
    print(bubbleSort(inp))