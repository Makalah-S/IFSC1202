secrets = open("Guessing Game/secrets")

import random
playerName = input("Enter Name: ")
numRange = int(input("What's the Maximum Number: "))
numAnswer = random.randint(1,numRange)
roundsLeft = 5

        

secrets.close