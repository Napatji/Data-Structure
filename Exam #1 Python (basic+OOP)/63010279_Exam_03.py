print(" *** String count ***")
user_input = input("Enter message : ").replace("."," ")
user_input = user_input.replace(" ","")
user_input = user_input.replace("'","")
user_input = user_input.replace(",","")
user_input = user_input.replace("#","")
upper_count = 0
lower_count = 0
upper_char = set()
lower_char = set()
for i in user_input:
    if i=="0" or i=="1" or i=="2" or i=="3" or i=="4" or i=="5" or i=="6" or i=="7" or i=="8" or i=="9":
        upper_count += 0
        lower_count += 0
    elif i == i.upper():
        upper_count += 1
        upper_char.add(i)
    elif i == i.lower():
        lower_count += 1
        lower_char.add(i)
upper_char = sorted(upper_char)
lower_char = sorted(lower_char)
print("No. of Upper case characters : {}".format(upper_count))
print("Unique Upper case characters : ",end="")
for i in upper_char:
    print(i,end="  ")
print("")
print("No. of Lower case Characters : {}".format(lower_count))
print("Unique Lower case characters : ",end="")
for i in lower_char:
    print(i,end="  ")
print("")