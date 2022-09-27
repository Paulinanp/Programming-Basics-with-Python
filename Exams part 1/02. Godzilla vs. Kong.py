budget = float(input())
count_statisti = int(input())
price_clothes_per_statist = float(input())

discount = 0

decor = budget * 0.1
price_clothes = count_statisti * price_clothes_per_statist

if count_statisti > 150:
    discount = price_clothes * 0.1
    price_clothes -= discount

final_sum = decor + price_clothes

if final_sum <= budget:
    money_left = budget - final_sum
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
else:
    money_need = final_sum - budget
    print("Not enough money!")
    print(f"Wingard needs {money_need:.2f} leva more.")