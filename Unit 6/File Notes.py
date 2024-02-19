demo = open("DemoText.txt") ##Opens a file, and enables its use.
x = demo.readline()

while x != "":
    print(x)
    x = demo.readline()

demo.close() ##Once a program is done using a file, always close it within the code.

new = open("Something New.txt", "w")
output = input("Write Something: ")

new.write(output + "/n")

print(new)
new.close()