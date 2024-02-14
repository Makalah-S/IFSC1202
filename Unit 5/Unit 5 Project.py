def findDigits(x): ##As of 09:58 2.12, Works as Intended. Not told to print.
    i = 0
    while x > 0:
        x = x//10
        i += 1
    return i

def isSpecial(input,lenght):
    exponet =  lenght
    orgi = input
    numSum = 0
    while lenght > 0:
        y = 10 ** (lenght - 1)
        indnumber = input//y
        numSum += indnumber ** exponet
        input -= indnumber * y
        lenght -= 1
    else:
        if numSum == orgi:
            return True
        else:
            return False

numberSum = 0

startOfRange = int(input("Enter Start of Range: "))
endOfRange = int(input("Enter End of Range: "))

print("These are the Special Numbers between {} and {}" .format(startOfRange, endOfRange))

for z in range(startOfRange, endOfRange+1):
    y = findDigits(z)
    if isSpecial(z,y) == True:
        print(z)