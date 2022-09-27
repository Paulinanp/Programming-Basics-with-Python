fruit = input()
size = input()
count = int(input())

price = 0
discount = 0


if fruit == "Watermelon":

    if size == "small":
        price = 2 * 56
    elif size == "big":
        price = 5 * 28.7

elif fruit == "Mango":

    if size == "small":
        price = 2 * 36.66
    elif size == "big":
        price = 5 * 19.60

elif fruit == "Pineapple":

    if size == "small":
        price = 2 * 42.10
    elif size == "big":
        price = 5 * 24.80

elif fruit == "Raspberry":

    if size == "small":
        price = 2 * 20
    elif size == "big":
        price = 5 * 15.20

final_price = price * count

if 400 <= final_price <= 1000:
    discount = 0.15 * final_price
    final_price -= discount
elif final_price > 1000:
    discount = 0.5 * final_price
    final_price -= discount

print(f"{final_price:.2f} lv.")