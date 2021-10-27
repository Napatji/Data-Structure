from itertools import combinations

def sum(arr):
    in_list = [] ###ตั้งlistเปล่า
    for i in arr: ### Add number to list
        in_list.append(int(i))
    sum_list =[] ### Answer
    ###Check in_list ว่าทุกตัวซ้ำกันมั้ย
    same_number = True ###Boolean ตัวซ้ำ
    check_sum = 0 ###ผลบวก
    for elements in range(0,len(in_list)):
        check_sum = check_sum + abs(in_list[elements])
    total = check_sum/len(in_list) ###หาค่าเฉลี่ย
    for num in in_list: ### check เรียงตัวว่าเหมือนกันมั้ย
        if abs(num) != total:
            same_number =False
    ###
    if len(in_list) < 3:
        return "Array Input Length Must More Than 2"
    elif same_number == True:
        in_list.sort()
        num_list = []
        num_list = combinations(in_list,3)### Permutation
        for i in num_list:
            j = list(i)
            if j[0]+j[1]+j[2] == 5:
                sum_list.append(j)
                break
        return sum_list
    else:
        num_list = []
        num_list = combinations(in_list,3)### Permutation
        for i in num_list:
            j = list(i)
            if j[0]+j[1]+j[2] == 5:
                sum_list.append(j)
        return sum_list          

if __name__ == "__main__":
    in_list = input("Enter Your List : ").split()
    print(sum(in_list))