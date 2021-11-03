def maxNum(num_list,endIndex):
    if endIndex == 1:
        return num_list[0]
    return  max(num_list[endIndex - 1], maxNum(num_list, endIndex - 1))

if __name__ == "__main__":
    inp = [int(i) for i in input('Enter Input : ').split()]
    print(f'Max : {maxNum(inp,len(inp)-1)}')