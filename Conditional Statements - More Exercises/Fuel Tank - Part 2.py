typeFuel = input()
fuelQuantity = float(input())
card = input()

price = 0
discount = 0

if card == "Yes":
    if typeFuel == "Gas":
        price = 0.93 * fuelQuantity - (fuelQuantity * 0.08)
    elif typeFuel == "Gasoline":
        price = 2.22 * fuelQuantity - (fuelQuantity * 0.18)
    elif typeFuel == "Diesel":
        price = 2.33 * fuelQuantity - (fuelQuantity * 0.12)
elif card == "No":
    if typeFuel == "Gas":
        price = 0.93 * fuelQuantity
    elif typeFuel == "Gasoline":
        price = 2.22 * fuelQuantity
    elif typeFuel == "Diesel":
        price = 2.33 * fuelQuantity

if 25 >= fuelQuantity >= 20:
    discount = price * 0.08
    price -= discount
elif fuelQuantity > 25:
    discount = price * 0.1
    price -= discount

print(f"{price:.2f} lv.")