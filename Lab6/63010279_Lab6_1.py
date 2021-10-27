def get_recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(get_recursive_fibonacci(n-1) + get_recursive_fibonacci(n-2))

if __name__ == "__main__":
    user_input = input("Enter Number : ")
    if int(user_input) > 0:
        print("fibo({0}) = {1}".format(user_input, get_recursive_fibonacci(int(user_input))))
    else:
        print("Please type positive number.")