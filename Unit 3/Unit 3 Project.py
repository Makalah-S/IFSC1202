x = float(input("First Number: "))
equation = input("Enter Operator (+, -, *, /): ")
y = float(input("Second Number: "))
answer = 0

if equation == '+':
    answer = x + y
elif equation == '-':
    answer = x - y
elif equation == '*':
    answer = x * y
elif equation == '/':
    answer = x/y
else:
    answer = "INVALID"

if answer == "INVALID":
    print("Invalid Operation")
else:
    print("{} {} {} = {}".format(x, equation, y, answer))