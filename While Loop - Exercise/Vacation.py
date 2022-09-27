price_for_trip = float(input())
money_that_have = float(input())
cons_spendings = 0
days_cnt = 0

while money_that_have < price_for_trip:
    action = input()
    amount = float(input())
    days_cnt += 1

    if action.lower() == "save":
        money_that_have += amount
        cons_spendings = 0
    elif action.lower() == "spend":
        if amount >= money_that_have:
            money_that_have = 0
        else:
            money_that_have -= amount

        cons_spendings += 1

        if cons_spendings == 5:
            break

if money_that_have >= price_for_trip:
    print(f"You saved the money for {days_cnt} days.")
else:
    print(f"You can't save the money.\n{days_cnt}")