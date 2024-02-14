import random
numberAnswer =  random.randint(1,20)
playersName = input("Name: ")
roundsLeft = 5

while roundsLeft > 0:
    print("Hey {}, you have {} rounds left!" .format(playersName, roundsLeft))
    numberGussed = int(input("Guess which number I'm thinking! It's between 1 and 20: "))
    if numberGussed > numberAnswer:
        print("Oops! Go lower!")
    elif numberGussed < numberAnswer:
        print("Oops! Go higher!")
    else:
        print("Oh! You got it, the number I was thinking was {}" .format(numberAnswer))
        break
    roundsLeft -= 1
else:
    print("Sorry, you couldn't get the right number in time {}. It was {}." .format(playersName, numberAnswer))