import requests
consitution = requests.get("https://www.usconstitution.net/const.txt")
consitutionText = consitution.text

readAgain = True

def findTerm(document):
    keyTerm = input("Enter search term: ")
    termNumber = document.find(keyTerm)
    termLocation = document[document.find(keyTerm)]
    




while readAgain == True:
    findTerm(consitutionText)