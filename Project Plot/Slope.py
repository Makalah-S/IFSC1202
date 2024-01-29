x = int(input("X-Value 1: "))
y = int(input("Y-Value 1: "))
a = int(input("X-Value 2: "))
b = int(input("Y-Value 2: "))

if b - y == 0:
    print("UNDEFINED")
else:
    SLOPE = (a - x)/(b - y)
    print("m = ",SLOPE)