budget = float(input())
fuel_need = float(input())
day = input()

discount = 0
guide = 100
total_fuel_price = fuel_need * 2.1

total_price = total_fuel_price + guide

if day == "Saturday":
    discount = total_price * 0.1
    total_price -= discount
elif day == "Sunday":
    discount = total_price * 0.2
    total_price -= discount

if budget > total_price:
    money_left = budget - total_price
    print(f"Safari time! Money left: {money_left:.2f} lv.")
else:
    money_need = total_price - budget
    print(f"Not enough money! Money needed: {money_need:.2f} lv.")