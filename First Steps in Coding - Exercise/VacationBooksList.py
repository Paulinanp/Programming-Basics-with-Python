import math

numberOfPages = int(input())
pagesPer1Hour = int(input())
numberOfDays = int(input())

allTimeForReading = numberOfPages / pagesPer1Hour
neededHoursPerDay = allTimeForReading / numberOfDays

print(math.floor(neededHoursPerDay))