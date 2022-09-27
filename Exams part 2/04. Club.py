profit = float(input())
money = 0
discount = 0
flag = False

curr_input = input()

while curr_input != "Party!":
    coctail_name = curr_input
    coctail_cnt = int(input())
    coctail_name_len = len(coctail_name)
    price_coctail = coctail_cnt * coctail_name_len
    money += coctail_name_len * coctail_cnt

    if price_coctail % 2 == 1:
        discount = money * 0.25
        money -= discount

    if money >= profit:
        flag = True
        print("Target acquired.")
        break

    curr_input = input()

if flag:
    print(f"Club income - {money:.2f} leva.")
else:
    money_need = abs(profit - money)
    print(f"We need {money_need:.2f} leva more.")
    print(f"Club income - {money:.2f} leva.")

