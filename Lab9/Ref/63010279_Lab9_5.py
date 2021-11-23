def recur(num,left,res,i=0,list=[]):
    sum=0
    pattern=0
    for j in list:
        sum+=j
    if left == 0:
        if res == sum:
            print(list)
            return 1
        return 0
    elif i>=len(num):
        return 0
    else:
        pattern+=recur(num,left-1,res,i+1,list+[num[i]])
        pattern+=recur(num,left,res,i+1,list)
    return pattern

if __name__ == '__main__':
    inp = input("Enter Input : ").split("/")
    res = int(inp[0])
    num = [int (x) for x in inp[1].split()]
    #sort
    for i in range(len(num)):
        for j in range(len(num)-1-i):
            if num[j]>num[j+1]:
                num[j],num[j+1]=num[j+1],num[j]
    pattern=0
    for j in range(len(num)):
        pattern+=recur(num,j+1,res)
    if pattern==0:
        print("No Subset")