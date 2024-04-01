city = []
chart =  open("Unit 9/09.Project Distances.csv")
chartText = chart.readline()
while chartText != "":
    readDocument = chartText.split(",")
    city.append(readDocument)
    chartText = chart.readline()

for ROW in range(len(city)):
    for COLOUM in range(len(city[ROW])):
        print(city[ROW][COLOUM], end=' ')


fromTown = input("Starting Point (Boston Buffalo Chicago Cleveland Dallas Denver Detroit El Paso Houston): ")
toTown = input("Ending Point (Boston Buffalo Chicago Cleveland Dallas Denver Detroit El Paso Houston) : ")

if fromTown in city == False:
    print("Invalid Starting Town")
else:
    if toTown in city == False:
        print("Invalid End Town")
    else:
        
        


chart.close