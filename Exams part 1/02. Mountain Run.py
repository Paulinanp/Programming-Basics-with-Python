from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_1m = float(input())

total_time = distance_in_meters * time_in_seconds_for_1m
delay = floor((distance_in_meters / 50)) * 30

final_time = total_time + delay

if final_time < record_in_seconds:
    print(f"Yes! The new record is {final_time:.2f} seconds.")
else:
    needed_time = final_time - record_in_seconds
    print(f"No! He was {needed_time:.2f} seconds slower.")
