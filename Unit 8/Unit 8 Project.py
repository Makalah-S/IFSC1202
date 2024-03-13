searchAgain = True
import requests
reponse = requests.get("https://www.usconstitution.net/const.txt")
responseText = reponse.text
consitution = responseText.split("\n")

##for i in range(len(consitution)):
    ##print(consitution[i])

def searchKeyTerm(document):
    keyTerm = input("Requested Term/Phrase: ")
    result = document.index(keyTerm)
    number = result
    while document.find(result) != " \n":
        result += 1
        print(document.index(result))
        
    print(document[number:result])

while searchAgain == True:
    searchKeyTerm(responseText)

    redo = input("Do you wish to search again? Yes or No: ")
    if redo != "yes":
        searchAgain = False