output = open("Unit 6/Unit 6 Project/06.Project Output File.txt", "a")

merge = open("Unit 6/Unit 6 Project/06.Project Merge File.txt")
y = merge.readline()

input = open("Unit 6/Unit 6 Project/06.Project Input File.txt")
x = input.readline()
change = "**Insert Merge File Here**\n"



while x != "":
    if x == change:
        print("Test sucessful")
    else:
        print(x)
        output.write(input.readline())
    x = input.readline()


input.close
output.close
merge.close