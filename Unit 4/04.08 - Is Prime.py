n = int(input("Enter Number: "))

for x in range(2,n//2+1):
    if n%x == 0:
        print("COMPOSITE")
        break
else:
        print("PRIME")

