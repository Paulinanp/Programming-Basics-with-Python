type_of_drink = input()
sugar = input()
drinks_count = int(input())

money = 0
discount = 0

if type_of_drink == "Espresso":
    if sugar == "Without":
        money = 0.9
    elif sugar == "Normal":
        money = 1
    elif sugar == "Extra":
        money = 1.2
elif type_of_drink == "Cappuccino":
    if sugar == "Without":
        money = 1
    elif sugar == "Normal":
        money = 1.2
    elif sugar == "Extra":
        money = 1.6
elif type_of_drink == "Tea":
    if sugar == "Without":
        money = 0.5
    elif sugar == "Normal":
        money = 0.6
    elif sugar == "Extra":
        money = 0.7

final_sum = money * drinks_count

if sugar == "Without":
    discount = final_sum * 0.35
    final_sum -= discount

if type_of_drink == "Espresso" and drinks_count >= 5:
    discount = final_sum * 0.25
    final_sum -= discount

if final_sum > 15:
    discount = final_sum * 0.2
    final_sum -= discount

print(f"You bought {drinks_count} cups of {type_of_drink} for {final_sum:.2f} lv.")