def odd_list(alist):
    check_list = []
    for element in alist:
        if (element % 2 != 0):
            check_list.append(element)
    return check_list

print(" ***Function Odd List***")
ls = [int(e) for e in input("Enter list numbers : ").split()]
opls = odd_list(ls)
print("Input list : ", ls, "\nOutput list : ", opls)

