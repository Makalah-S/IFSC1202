searchAgain = True
import requests
consitution = requests.get("https://www.usconstitution.net/const.txt")

def searchKeyTerm(document):
    keyTerm = input("Requested Term/Phrase: ")

while searchAgain == True:
    searchKeyTerm(consitution)

    redo = input("Do you wish to search again? Yes or No")
    print(redo)
    if redo != "Yes":
        searchAgain = False