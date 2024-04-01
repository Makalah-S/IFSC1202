city = []
chart =  open("Unit 9/09.Project Distances.csv")
chartText = chart.readline()
while chartText != "":
    readDocument = chartText.split(",")
    city.append(readDocument)
    chartText = chart.readline()
else:
    print(city)

chart.close