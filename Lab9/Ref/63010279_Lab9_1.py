if __name__=="__main__":
    inp = input("Enter Input : ").split(" ")
    c=True
    for k in range(len(inp)-1):
        if inp[k]>inp[k+1]:
            c=False
    if c==True:
        print("last step : [{}] move[None]".format(', '.join(map(str, inp))))
    else:
        for i in range(len(inp)-1):
            move=inp[0]
            for j in range(len(inp)-i-1):
                if int(inp[j])>int(inp[j+1]):
                    inp[j],inp[j+1]=inp[j+1],inp[j]
                    move=inp[j+1]
            if i==len(inp)-2:
                print("last step : [{}] move[{}]".format(', '.join(map(str, inp)),move)) 
            else :
                print("{} step : [{}] move[{}]".format(i+1,', '.join(map(str, inp)),move))
            #check sort
            c=True
            for k in range(len(inp)-1):
                if inp[k]>inp[k+1]:
                    c=False
            if c is True:
                break
        if i!=len(inp)-2:
            print("last step : [{}] move[None]".format(', '.join(map(str, inp))))