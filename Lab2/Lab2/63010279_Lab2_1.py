def Rshift(num,shift):
    return num>>shift

if __name__ == "__main__":
    n,s = input("Enter number and shiftcount : ").split()
    print(Rshift(int(n),int(s)))