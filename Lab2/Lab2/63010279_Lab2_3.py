def mod_position(arr, s):
    in_list = []
    out_list = []
    in_list.extend(arr)
    for i in range(len(in_list)):
        if (i + 1) % int(s) == 0:
            out_list.append(in_list[i])
    return out_list
    
if __name__ == "__main__":
    print("*** Mod Position ***")
    arr,s = input("Enter Input : ").split(",")
    print(mod_position(arr, s))