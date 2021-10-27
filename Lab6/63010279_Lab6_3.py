def gcd(num1, num2):
    if num2 == 0:
        return num1
    else:
        return abs(gcd(num2, num1 % num2))
        
if __name__ == "__main__":
    num1, num2 = input("Enter Input : ").split()
    if int(num1) == 0 and int(num2) == 0:
        print("Error! must be not all zero.")
    else:
        print("The gcd of {0} and {1} is : {2}".format(num1, num2, gcd(int(num1), int(num2))) if num1 > num2 else "The gcd of {0} and {1} is : {2}".format(num2, num1, gcd(int(num1), int(num2))))