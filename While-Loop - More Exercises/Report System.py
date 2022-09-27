budget = int(input())

counter = 1
pay_card_cnt = 0
pay_cash_cnt = 0
pay_cash_money = 0
pay_card_money = 0
total_sum = 0

curr_input = input()
while curr_input != "End":
    money = int(curr_input)

    if counter % 2 != 0:
        if money > 100:
            print("Error in transaction!")
        else:
            print("Product sold!")
            pay_cash_money += money
            pay_cash_cnt += 1
    else:
        if money < 10:
            print("Error in transaction!")
        else:
            print("Product sold!")
            pay_card_money += money
            pay_card_cnt += 1

    total_sum = pay_card_money + pay_cash_money

    if total_sum >= budget:
        print(f"Average CS: {pay_cash_money / pay_cash_cnt:.2f}")
        print(f"Average CC: {pay_card_money / pay_card_cnt:.2f}")
        break

    counter += 1
    curr_input = input()

if total_sum < budget:
    print("Failed to collect required money for charity.")