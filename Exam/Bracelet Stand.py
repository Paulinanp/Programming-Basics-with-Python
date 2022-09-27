budget_per_day = float(input())
earn_money_per_day = float(input())
cost_money = float(input())
price_for_gift = float(input())

saved_money = budget_per_day * 5
all_earn_money = earn_money_per_day * 5

total_saved_money = saved_money + all_earn_money
left_money = total_saved_money - cost_money

if left_money >= price_for_gift:
    print(f"Profit: {left_money:.2f} BGN, the gift has been purchased.")
else:
    money_need = price_for_gift - left_money
    print(f"Insufficient money: {money_need:.2f} BGN.")