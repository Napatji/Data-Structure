def harmonic_sum(n):
    if n == 0:
        return 0
    if n == 1:
        print("1", end='')
        return 1/n
    else:
        temp = 1/n + harmonic_sum(n-1)
        print(f' + 1/{n}', end='')
        return temp

print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
print(" = %.8f" %(harmonic_sum(num)))