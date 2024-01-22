s = int(input("How Many Numbers?"))
n = s
v = 0

while n > 0:
    v = int(input("What's the Number?")) + v
    n = n - 1

a = v/s

print(a)