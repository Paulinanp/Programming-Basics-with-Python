guests_count = int(input())
price_envelope = float(input())
budget = float(input())

discount = 0

if 10 <= guests_count <= 15:
    discount = price_envelope * 0.15
    price_envelope -= discount
elif 15 < guests_count <= 20:
    discount = price_envelope * 0.2
    price_envelope -= discount
elif guests_count > 20:
    discount = price_envelope * 0.25
    price_envelope -= discount

price_cake = budget * 0.1

final_price = (guests_count * price_envelope) + price_cake

if budget >= final_price:
    money_left = budget - final_price
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_need = final_price - budget
    print(f"No party! {money_need:.2f} leva needed.")