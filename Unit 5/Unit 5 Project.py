n = int(input("Enter a Number: "))

def findDigits (x): ##As of 09:58 2.12, Works as Intended. Not told to print.
    i = 0
    while x > 0:
        x = x//10
        i += 1
    return i


