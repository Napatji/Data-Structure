def harmonic_sum(start,n):
    if start <= n:
        if start == 1:
            if n != 1:
                print(f'1',end=' + ')
                return 1 + (harmonic_sum(start+1,n))
            else:
                print(f'1',end=' = ')
                return 1
        elif start < n :
            print(f'1/{start}',end=' + ')
            return 1 / start + (harmonic_sum(start+1,n))
        elif start == n:
            print(f'1/{start}',end=' = ')
            return 1 / start

if __name__ == "__main__":
    print(' *** Harmonic sum ***')
    num = int(input("Enter number of terms : ")) 
    print("%.8f" %(harmonic_sum(1,num)))