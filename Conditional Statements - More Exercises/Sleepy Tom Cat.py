daysOff = int(input())
time_that_kitty_needs_for_games = 30000

workingdays = 365 - daysOff

timeForGames = (daysOff * 127) + (workingdays * 63)

timeLeft = abs(time_that_kitty_needs_for_games - timeForGames)

timeInHours = timeLeft // 60
timeInMinutes = timeLeft % 60

if timeForGames <= time_that_kitty_needs_for_games:
    print("Tom sleeps well")
    print(f"{timeInHours} hours and {timeInMinutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{timeInHours} hours and {timeInMinutes} minutes more for play")