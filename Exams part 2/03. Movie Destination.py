budget = float(input())
destination = input()
season = input()
days = int(input())

price = 0
discount = 0

if destination == "Dubai":

    if season == "Winter":
        price = 45000
    elif season == "Summer":
        price = 40000

elif destination == "Sofia":

    if season == "Winter":
        price = 17000
    elif season == "Summer":
        price = 12500

elif destination == "London":

    if season == "Winter":
        price = 24000
    elif season == "Summer":
        price = 20250

price *= days

if destination == "Dubai":
    discount = price * 0.3
    price -= discount

if destination == "Sofia":
    discount = price * 0.25
    price += discount

if budget >= price:
    money_left = budget - price
    print(f"The budget for the movie is enough! "
          f"We have {money_left:.2f} leva left!")
else:
    money_need = price - budget
    print(f"The director needs {money_need:.2f} leva more!")

