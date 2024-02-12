x = int(input("Enter Number 1000: "))
i = 0

print(1000//10)
print(100//10)
print(10//10)
print(0/10)

while x > 0: ##Counts Digits
    x = x//10
    i += 1
    print(i)
