a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Prime Numbers Between {} and {}" .format(a,b))

def findPrime(n):
    for x in range(2,n//2+1):
        if n%x == 0:
            return False #For Composites
            break
    else:
            return True #For Primes

for i in range(a,b):
     if findPrime(i) == True:
          print(i)