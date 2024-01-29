x = float(input("Next Whole Number: "))
if x%1 != 0:
    x = x//1 + 1
print(x)