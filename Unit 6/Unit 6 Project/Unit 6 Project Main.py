output = open("Unit 6/Unit 6 Project/06.Project Output File.txt", "a")
merge = open("Unit 6/Unit 6 Project/06.Project Merge File.txt")
input = open("Unit 6/Unit 6 Project/06.Project Input File.txt")

change = "**Insert Merge File Here**\n"

x = input.readline()
y = merge.readline()

numInput = 0
numMerge = 0

while x != "":
    if x == change:
        while y != "":
            print(y)
            output.write(y)
            y = merge.readline()
            numMerge += 1
        else:
            merge.close()
    else:
        print(x)
        output.write(x)
        numInput += 1
    x = input.readline()    
else:
    input.close()
    output.close()

print("{} input files recorded.\n{} merge files recorded.\n{} output files recorded." .format(numInput,numMerge,numMerge+numInput))

