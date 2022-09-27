hour = int(input())
day = input()

working_days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
days_off = "Sunday"

if day in working_days:
    if 10 <= hour <= 18:
        print("open")
    else:
        print("closed")
elif day in days_off:
    print("closed")