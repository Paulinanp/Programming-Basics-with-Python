from math import ceil

guest_count = int(input())
budget = int(input())

easter_bread_count = ceil(guest_count / 3)
easter_bread_price = easter_bread_count * 4

eggs_count = guest_count * 2
eggs_price = eggs_count * 0.45

final_price = eggs_price + easter_bread_price

if budget >= final_price:
    money_left = budget - final_price
    print(f"Lyubo bought {easter_bread_count} Easter "
          f"bread and {eggs_count} eggs."
          f"\nHe has {money_left:.2f} lv. left.")
else:
    money_need = final_price - budget
    print(f"Lyubo doesn't have enough money."
          f"\nHe needs {money_need:.2f} lv. more.")