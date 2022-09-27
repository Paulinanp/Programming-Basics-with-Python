hours = int(input())
minutes = int(input())

hoursInMins = hours * 60

totalTimeInMins = minutes + hoursInMins + 15

timeInHours = totalTimeInMins // 60
timeInMins = totalTimeInMins % 60

if timeInHours > 23:
    timeInHours = 0

if timeInMins < 10:
    print(f"{timeInHours}:0{timeInMins}")
else:
    print(f"{timeInHours}:{timeInMins}")