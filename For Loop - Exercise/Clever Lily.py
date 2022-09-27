lily_age = int(input())
washer_price = float(input())
toy_price = int(input())

toys_count = 0
total_money = 0

for age in range(1, lily_age + 1):

    if age % 2 == 0:
        money = (age * 5) - 1
        total_money += money
    else:
        toys_count += 1

earn_money = toy_price * toys_count + total_money

if earn_money >= washer_price:
    money_left = earn_money - washer_price
    print(f"Yes! {money_left:.2f}")
else:
    money_need = washer_price - earn_money
    print(f"No! {money_need:.2f}")