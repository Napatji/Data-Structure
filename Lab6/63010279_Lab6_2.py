def length(txt, count = 0):
    first = ""
    if txt[1:] != "":
        first = txt[0]
        second = txt[1]
        txt = txt[2:]
        return 2 + length(txt)[0] , (first + "*" + second + "~" + str(length(txt)[1])) 
        #return 1 + length(txt)[0] , (first + "*" + str(length(txt)[1])) 
    elif txt != "":
        return 1 , str(txt + "*")
    else:
        return 0 , ""
        
if __name__ == "__main__":
    user_input = input("Enter Input : ")
    print(length(user_input)[1])
    print(length(user_input)[0])