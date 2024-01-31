x = float(input("First Number: "))
y = float(input("Second Number: "))
equation = input("Choose from the Following: +, -, *, /")
answer = 0

if equation == '+':
    answer = x + y
elif equation == '-':
    answer = x - y
elif equation == "*":
    answer = x * y
elif equation == '/':
    answer = x/y
else:
    print("Invalid Operation")

print(answer)