print("*** String Rotation ***")
one,two = input("Enter 2 strings : ").split(" ")
first = one
second = two
one_check = False
two_check = False
count = 0
while one_check == False and two_check == False:
    temp1 = one[-1]
    one = one[0:-1]
    one = temp1+one
    temp2 = two[-1]
    two = two[0:-1]
    two = temp2+two
    count += 1
    print("{0} {1} {2}".format(count,one,two))
    if first == one and second == two:
        one_check = True
        two_check = True
print("Total of  {} rounds.".format(count))