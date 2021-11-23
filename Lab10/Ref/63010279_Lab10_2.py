inp = input('Enter Input : ').split('/')
left,right = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for r in right:
    fgt=1000001
    for l in left:
        if l>r and l<fgt:
            fgt = l
    if fgt==1000001:
        print("No First Greater Value")
    else:
        print(fgt)