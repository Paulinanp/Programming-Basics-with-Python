count_km = int(input())
time = input()

ticketPrice = 0

if count_km < 20:
    if time == "day":
        ticketPrice = count_km * 0.79 + 0.7
    elif time == "night":
        ticketPrice = 0.7 + count_km * 0.9
elif 100 > count_km >= 20:
    ticketPrice = count_km * 0.09
else:
    ticketPrice = count_km * 0.06

print(f"{ticketPrice:.2f}")

