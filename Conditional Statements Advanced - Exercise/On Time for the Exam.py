hour_exam = int(input())
minutes_exam = int(input())
hour_arrived = int(input())
minutes_arrived = int(input())

exam_time_in_mins = hour_exam * 60 + minutes_exam
arrived_time_in_mins = hour_arrived * 60 + minutes_arrived

time_diff = abs(exam_time_in_mins - arrived_time_in_mins)

if exam_time_in_mins < arrived_time_in_mins:
    print("Late")
    if time_diff >= 60:
        hours_late = time_diff // 60
        mins_late = time_diff % 60
        if mins_late < 10:
            print(f"{hours_late}:0{mins_late} hours after the start")
        else:
            print(f"{hours_late}:{mins_late} hours after the start")
    else:
        print(f"{time_diff} minutes after the start")
elif exam_time_in_mins >= arrived_time_in_mins and time_diff <= 30:
    print("On time")
    if time_diff > 0:
        print(f"{time_diff} minutes before the start")
else:
    print("Early")

    if time_diff >= 60:
        hours_early = time_diff // 60
        minutes_early = time_diff % 60

        print(f"{hours_early}:{minutes_early:02d} hours before the start")
    else:
        print(f"{time_diff} minutes before the start")