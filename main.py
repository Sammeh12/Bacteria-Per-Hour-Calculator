countOfBacteria = int(input("Enter initial count of bacteria: "))
numberOfHours = int(input("Enter the number of hours: "))

totalHours = numberOfHours * 60
generationTime = totalHours / 20
givenTime = numberOfHours ** generationTime

binaryFission = countOfBacteria * givenTime

print("The number of bacteria per hour will be:")
for i in range(1, 6):
    countOfHours = "Hour " + str(i) + " = "
    bacteriaPerHour = i * givenTime
    convertBctrPrHr = str(bacteriaPerHour)
    print(countOfHours + convertBctrPrHr)
