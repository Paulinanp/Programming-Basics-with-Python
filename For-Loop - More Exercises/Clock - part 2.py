secs = 0
mins = 0
hours = 0

while hours != 24 and mins != 60 and secs != 60:
    print(f"{hours} : {mins} : {secs}")

    secs += 1

    if secs == 60:
        secs = 0
        mins += 1

    if mins == 60:
        mins = 0
        hours += 1