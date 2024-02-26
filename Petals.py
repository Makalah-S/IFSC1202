def isSpecial(input,lenght):
    exponet =  lenght
    copy = input
    numSum = 0
    while lenght > 0:
        y = 10 ** (lenght - 1)
        indnumber = input//y
        numSum += indnumber ** exponet
        input -= indnumber * y
        lenght -= 1
    else:
        if numSum == copy:
            return True
        else:
            return False

def findDigits(x): ##As of 09:58 2.12, Works as Intended. Not told to print.
    i = 0
    while x > 0:
        x = x//10
        i += 1
    return i

def findPrime(n):
    for x in range(2,n//2+1):
        if n%x == 0:
            return False #For Composites
            break
    else:
            return True #For Primes
    
def prime_composite(n):
    print("Number Given: {}" .format(n))
    for x in range(2,n//2+1):
        if n%x == 0:
            print("COMPOSITE")
            break
    else:
        print("PRIME")


def readFileLines(DOCUMENT):
    n = DOCUMENT.readline()
    while n != "":
        print(n)
        n = DOCUMENT.readline()