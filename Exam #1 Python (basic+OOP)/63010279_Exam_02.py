print(" *** Divisible number ***")
user_input = int(input("Enter a positive number : "))
if user_input <= 0:
    print("{0} is OUT of range !!!".format(user_input))
else:
    divisible = []
    count = 0
    print("Output ==> ",end="")
    for i in range(1,user_input+1):
        if user_input % i == 0:
            print(i,end=" ")
            count += 1
    print("")
    print("Total ==> {0}".format(count))