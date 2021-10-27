def weirdSubtract(n,k):
    for i in range(0,k):
        if(n % 10 ==0):
            n = n / 10
        else:
            n = n - 1
    return int(n)


if __name__ == "__main__":
    n,s = input("Enter num and sub : ").split()
    print(weirdSubtract(int(n),int(s)))