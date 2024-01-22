s = int(input("How Many Numbers?")) ## Program Finds the Mean of a Set of Numbers, Practice for User Input
n = s
v = 0

while n > 0:
    v = int(input("What's the Number?")) + v
    n = n - 1
    print("Entries Left:", n)

a = v/s

print("Mean:", a)