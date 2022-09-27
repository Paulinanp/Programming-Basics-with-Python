budget = float(input())
nights_count = int(input())
night_price = float(input())
extra_money_percent = int(input())

discount = 0

if nights_count > 7:
    discount = night_price * 0.05
    night_price -= discount

total_price_nights = night_price * nights_count
extra_money = budget * extra_money_percent / 100

final_price = total_price_nights + extra_money

if final_price <= budget:
    money_left = budget - final_price
    print(f"Ivanovi will be left with {money_left:.2f} leva after vacation.")
else:
    money_need = final_price - budget
    print(f"{money_need:.2f} leva needed.")