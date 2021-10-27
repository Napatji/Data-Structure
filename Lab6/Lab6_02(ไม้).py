def length(txt):
    if txt[1:] !="":
        print(txt[0],end="")
        print("*",end="")
        print(txt[1],end="")
        print("~",end="")
        txt=txt[2:]
        return 2+length(txt)
    elif txt !="":
        print(txt[0],end="")
        print("*",end="")
        txt=txt[1:]
        return 1+length(txt)
    else:
        return 0
print("\n",length(input("Enter Input : ")),sep="")