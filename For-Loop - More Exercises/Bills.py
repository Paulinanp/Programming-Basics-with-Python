months = int(input())

electricity = 0
water = 0
internet = 0
other = 0
average = 0

for month in range(months):
    bill_for_electricity = float(input())

    electricity += bill_for_electricity

water = months * 20
internet = months * 15
other += (electricity + water + internet) * 1.20
average = (electricity + water + internet + other) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {other:.2f} lv")
print(f"Average: {average:.2f} lv")