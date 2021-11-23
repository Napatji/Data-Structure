

def candice(good,weight,box):
    gooditr=0
    for i in range(box):
        weightinbox=0
        while True:
            if gooditr==len(good):
                return True
            if weight>=good[gooditr]+weightinbox:
                weightinbox=weightinbox+good[gooditr]
                gooditr+=1
            else:
                break
    return False

if __name__=="__main__":
    inp=input("Enter Input : ").split("/")
    good=[]
    for i in inp[0].split(" "):
        good.append(int(i))
    box=int(inp[1])
    weight=0
    for i in good:
        if i>weight:
            weight=i
    while candice(good,weight,box) is False:
        weight+=1
    print("Minimum weigth for {} box(es) = {}".format(box,weight))