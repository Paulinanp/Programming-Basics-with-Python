price_for_backpack_over_20kg = float(input())
backpack_kg = float(input())
trip_days = int(input())
backpack_count = int(input())

tax = 0

if backpack_kg <= 10:
    tax = price_for_backpack_over_20kg * 0.2
elif 10 < backpack_kg <= 20:
    tax = price_for_backpack_over_20kg * 0.5
elif backpack_kg > 20:
    tax = price_for_backpack_over_20kg

if trip_days > 30:
    tax += (tax * 0.1)
elif 7 <= trip_days <= 30:
    tax += tax * 0.15
elif trip_days < 7:
    tax += tax * 0.4

final_sum = tax * backpack_count

print(f"The total price of bags is: {final_sum:.2f} lv.")