days = int(input("Number of Days: "))

years = days//365
week = (days%365)//7
days = (days%365)%7

print("Years: ", years)
print("Weeks:", week)
print("Days: ", days)