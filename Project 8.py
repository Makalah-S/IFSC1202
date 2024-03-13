def findTerm(document):
    readDocument = document.split("\n")
    searchTerm = input("Hello! Enter a Search Term: ")
    if searchTerm == "":
        return ""
    for i in range(len(readDocument)): #Reads the entirety of the Document
        termPosition = readDocument[i].find(searchTerm) #Returns the line in which the term is found.
        if termPosition != -1: #-1 means the term cannot be found within the document. Try lower case!
            for j in range(i,0,-1):
                if readDocument[j] == "": #Moves back until an empty space is discovered
                    sectionStart = j #The sentence in which begins the section.
                    break #You want want it to continue in the loop, so break it off here.
            for k in range(i,len(readDocument)): #From the sentence the term was located to the end.
                if readDocument[k] == "": #Moves forward to end section, no need to add third modifier.
                    sectionEnd = k
                    break
            for m in range(sectionStart,sectionEnd): #Remeber, they still repersent numbers.
                print(readDocument[m]) #Weird looking, I know. But it can work in such formating.

import requests
reponse = requests.get("https://www.usconstitution.net/const.txt")
consitution = reponse.text

searchAgain = True

while searchAgain == True:
    findTerm(consitution)
    if findTerm(consitution) == "":
        break