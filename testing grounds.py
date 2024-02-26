output = open("Unit 6/Unit 6 Project/06.Project Output File.txt", "a")

merge = open("Unit 6/Unit 6 Project/06.Project Merge File.txt")
##y = merge.readline()

input = open("Unit 6/Unit 6 Project/06.Project Input File.txt")
##x = input.readline()

def lineCOUNT(FILE):
    n = FILE.readline()
    COUNT = 0
    while n != "":
        COUNT += 1
        n = FILE.readline()
    return COUNT

print(lineCOUNT(input))

input.close
merge.close
input.close 