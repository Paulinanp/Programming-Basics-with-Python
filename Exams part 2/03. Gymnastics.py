country = input()
type = input()

difficulty = 0
execution = 0

if type == "ribbon":

    if country == "Russia":
        difficulty = 9.100
        execution = 9.400
    elif country == "Bulgaria":
        difficulty = 9.600
        execution = 9.400
    elif country == "Italy":
        difficulty = 9.200
        execution = 9.500

elif type == "hoop":

    if country == "Russia":
        difficulty = 9.300
        execution = 9.800
    elif country == "Bulgaria":
        difficulty = 9.550
        execution = 9.750
    elif country == "Italy":
        difficulty = 9.450
        execution = 9.350

elif type == "rope":

    if country == "Russia":
        difficulty = 9.600
        execution = 9.000
    elif country == "Bulgaria":
        difficulty = 9.500
        execution = 9.400
    elif country == "Italy":
        difficulty = 9.700
        execution = 9.150

total_score = difficulty + execution
needed_percent = (20 - total_score) / 20 * 100

print(f"The team of {country} get {total_score:.3f} on {type}.")
print(f"{needed_percent:.2f}%")