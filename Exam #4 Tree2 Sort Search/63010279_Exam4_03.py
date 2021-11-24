def insertion(numlist):
    step = 0 # count step 
    for i in numlist:
        pass
    return step

def checkSort(numlist):
    check = True
    for i in range(0,len(numlist)-1):
        if int(numlist[i]) > int(numlist[i+1]):
            check = False
    return check

if __name__ == '__main__':
    print(' *** Insertion sort ***')
    inp = input('Enter some numbers : ').split(' ')
    inp = list(map(int,inp))
    step = insertion(inp)
    print(' ')
    print(f'{inp}')
    print(f'Data comparison = {step}')