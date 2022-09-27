firstTime = int(input())
secondTime = int(input())
thirdTime = int(input())

totalTimeInSeconds = firstTime + secondTime + thirdTime
timeInMins = totalTimeInSeconds // 60
timeInSecs = totalTimeInSeconds % 60

if timeInSecs < 10:
    print(f"{timeInMins}:0{timeInSecs}")
else:
    print(f"{timeInMins}:{timeInSecs}")
