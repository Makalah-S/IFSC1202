
lenght = 3
exponet = 3
input = 153
numSum = 0

## 1 + 

while lenght > 0:
    y = 10 ** (lenght - 1)
    indnumber = input//y
    numSum += indnumber ** exponet
    print(numSum)
    input -= indnumber * y
    lenght -= 1

