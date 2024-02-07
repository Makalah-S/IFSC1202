a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Prime Numbers Between {} and {}" .format(a,b))

def findPrime(n):
    for x in range(2,n//2+1):
        if n%x == 0:
            #print("COMPOSITE")
            return False
            break
    else:
            #print("PRIME")
            return True

for i in range(a,b):
     if findPrime(i) == True:
          print(i)