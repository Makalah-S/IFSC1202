import requests
reponse = requests.get("https://www.usconstitution.net/const.txt")
consitution = reponse.text
readConsitution = consitution.split("\n")

startAgain = True

searchTerm = input("Enter Search Term: ")
sectionStart = 0
sectionEnd = 0
for i in range(len(readConsitution)):
    pos = readConsitution[i].find(searchTerm)
    if pos != -1:
#        print(readConsitution[i])
        for j in range(i, 0, -1):
            if readConsitution[j] == "":
                sectionStart = j
                break
        for k in range(i,len(readConsitution)):
            if readConsitution[k] == "":
                sectionEnd = k
                break
        for m in range(sectionStart, sectionEnd):
            print(readConsitution[m])







