from math import ceil

name_of_series = input()
time_of_episode = int(input())
time_for_break = int(input())

time_for_lunch = 1/8 * time_for_break
time_for_relax = 1/4 * time_for_break

total_time = time_for_lunch + time_for_relax + time_of_episode

if time_for_break >= total_time:
    timeLeft = time_for_break - total_time
    print(f"You have enough time to watch {name_of_series} "
          f"and left with {ceil(timeLeft)} minutes free time.")
else:
    timeNeeded = total_time - time_for_break
    print(f"You don't have enough time to watch {name_of_series},"
          f" you need {ceil(timeNeeded)} more minutes.")