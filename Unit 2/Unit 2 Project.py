import math ## Have to summon library math in order to do equations

a = float(input("Enter Side A: "))
b = float(input("Enter Side B: "))
c = float(input("Enter Side C: "))
s = (a + b + c)/2

AREA = math.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area: {}" .format(AREA))

## Computer needs to be told that the problem is multiplication, couldn't assume from ()
## Important to note for Project Plot