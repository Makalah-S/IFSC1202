##So pretty much, here's the case. Our base responds is to check and see if the number is prime.
##If that number is prime, the function will return a TRUE statement.
##It will be within a loop channel, so it'll most likely be checking X and not N.
##User input choosing the starting number and the end.

a = int(input("Enter Start of Range: "))
b = int(input("Enter End of Range: "))
print("Prime Numbers Between {} and {}" .format(a,b))

def checkprime(n):
    for x in range(2,n//2+1):
        if n%x == 0:
            return False
        else:
            return True

for i in range(a,b):
    if checkprime(i) == False:
        print(i)
