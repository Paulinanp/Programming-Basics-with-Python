record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_secs_that_swim_for_1m = float(input())

time_that_swim_in_secs = distance_in_meters * time_in_secs_that_swim_for_1m

slow = distance_in_meters // 15
slowTimeInSecs = slow * 12.5

totalTime = time_that_swim_in_secs + slowTimeInSecs

if record_in_seconds > totalTime:
    print(f"Yes, he succeeded! The new world record is {totalTime:.2f} seconds.")
else:
    timeLeft = totalTime - record_in_seconds
    print(f"No, he failed! He was {timeLeft:.2f} seconds slower.")