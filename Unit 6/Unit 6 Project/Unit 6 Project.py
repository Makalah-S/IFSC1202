input = open("Unit 6/Unit 6 Project/06.Project Input File.txt")
merge = open("Unit 6/Unit 6 Project/06.Project Merge File.txt")

change = "**Insert Merge File Here**\n"

y = 0

def readFileLines(DOCUMENT):
    n = DOCUMENT.readline()
    while n != "":
        n = DOCUMENT.readline()
        print(n)

x = input.readlines()

while x != "":
    print(x)
    x = input.readline()

input.close
merge.close
