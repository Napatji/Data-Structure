def somethingDrome(numlist):
    sort1 = isSort1(numlist)
    sort2 = isSort2(numlist)
    dup = isDuplicate(numlist)
    #Repdrome => เลขตัวเดียวกันหมด
    if len(set(numlist)) == 1:
        print('Repdrome')
    #Metadrome => น้อยไปมาก and ไม่มีตัวซ้ำ
    elif sort1 == True and dup == False:
        print('Metadrome')
    #Plaindrome => น้อยไปมาก and มีตัวซ้ำ
    elif sort1 == True and dup == True:
        print('Plaindrome')
    #Katadrome => มากไปน้อย and ไม่มีตัวซ้ำ
    elif sort2 == True and dup == False:
        print('Katadrome')
    #Nialpdrome => มากไปน้อย and มีตัวซ้ำ
    elif sort2 == True and dup == True:
        print('Nialpdrome')
    #Nondrome => ไม่อยู่ในเงื่อนไขด้านบน
    else:
        print('Nondrome')

#น้อยไปมาก
def isSort1(numlist):
    check = True
    for i in range(0,len(numlist)-1):
        if int(numlist[i]) > int(numlist[i+1]):
            check = False
    return check

#มากไปน้อย
def isSort2(numlist):
    check = True
    for i in range(0,len(numlist)-1):
        if int(numlist[i]) < int(numlist[i+1]):
            check = False
    return check

def isDuplicate(numlist):
    check = False
    set_num = set(numlist)
    if len(set_num) != len(numlist):
        check = True
    return check

if __name__ == '__main__':
    inp = [int(i) for i in input('Enter Input : ')]
    # print(inp)
    # print(isSort2(inp))
    # print(isDuplicate(inp))
    somethingDrome(inp)