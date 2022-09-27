day = input()

is_working_day = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday"]
is_weekend = ["Saturday", "Sunday"]

if day in is_working_day:
    print("Working day")
elif day in is_weekend:
    print("Weekend")
else:
    print("Error")