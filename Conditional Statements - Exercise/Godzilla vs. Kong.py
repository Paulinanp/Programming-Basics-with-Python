budget = float(input())
count_statisti = int(input())
price_for_clothe_per_a_statist = float(input())

discount = 0
decor = budget * 0.1
price_clothes = count_statisti * price_for_clothe_per_a_statist

total_price = decor + price_clothes

if count_statisti > 150:
    discount = price_clothes * 0.1
    total_price -= discount

if total_price <= budget:
    moneyLeft = budget - total_price
    print("Action!")
    print(f"Wingard starts filming with {moneyLeft:.2f} leva left.")
else:
    moneyNeeded = total_price - budget
    print("Not enough money!")
    print(f"Wingard needs {moneyNeeded:.2f} leva more.")