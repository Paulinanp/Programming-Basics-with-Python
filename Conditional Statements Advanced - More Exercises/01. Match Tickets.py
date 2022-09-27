budget = float(input())
category = input()
people_count = int(input())

price_tickets = 0
total_sum = 0
fuel = 0

if category == "VIP":
    price_tickets = 499.99
    total_sum = price_tickets * people_count
elif category == "Normal":
    price_tickets = 249.99
    total_sum = price_tickets * people_count

if 1 <= people_count <= 4:
    fuel = budget * 0.75
elif 5 <= people_count <= 9:
    fuel = budget * 0.6
elif 10 <= people_count <= 24:
    fuel = budget * 0.5
elif 25 <= people_count <= 49:
    fuel = budget * 0.4
elif people_count > 49:
    fuel = budget * 0.25

final_sum = total_sum + fuel

if final_sum <= budget:
    money_left = budget - final_sum
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_need = final_sum - budget
    print(f"Not enough money! You need {money_need:.2f} leva.")
