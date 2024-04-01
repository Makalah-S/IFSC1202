import math

properties = []
zipcodes = []

propertiesList = open("Exam 2/Exam Two Properties.csv")
propertiesText = propertiesList.readline()


while propertiesText != "":
    readProperties = propertiesText.split(",")
    properties.append(readProperties)
    propertiesText = propertiesList.readline()


for ROW in range(len(properties)):
    for COLOUM in range(len(properties[ROW])):
        zip = properties[ROW][3]
        if (properties[ROW][3] in zipcodes) == False:
            zipcodes.append(zip)


for ROW in range(len(zipcodes)):
    for COLOUM in range(len(zipcodes[ROW])):
        print(zipcodes[ROW][COLOUM], end='')
    print()


propertiesList.close