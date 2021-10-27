from itertools import combinations
in_list = [5, -5, 5, -5, 5, -5, 5, 5, -5, -5, -5, -5, 5]
sum_list = []
num_list = combinations(in_list,3)
for i in num_list:
    j = list(i)
    if j[0]+j[1]+j[2] == 5:
        sum_list.append(j)
print(sum_list)