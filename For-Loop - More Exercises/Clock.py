mins = 0
hours = 0

while hours != 24 and mins != 60:
    print(f"{hours} : {mins}")
    mins += 1

    if mins == 60:
        mins = 0
        hours += 1
