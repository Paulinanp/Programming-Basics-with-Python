contraction = input()
type_of_contraction = input()
mobile_internet = input()
months = int(input())

price = 0
discount = 0

if contraction == "one":

    if type_of_contraction == "Small":
        price = 9.98
    elif type_of_contraction == "Middle":
        price = 18.99
    elif type_of_contraction == "Large":
        price = 25.98
    elif type_of_contraction == "ExtraLarge":
        price = 35.99

elif contraction == "two":

    if type_of_contraction == "Small":
        price = 8.58
    elif type_of_contraction == "Middle":
        price = 17.09
    elif type_of_contraction == "Large":
        price = 23.59
    elif type_of_contraction == "ExtraLarge":
        price = 31.79

if mobile_internet == "yes":
    if price <= 10:
        price += 5.5
    elif price <= 30:
        price += 4.35
    else:
        price += 3.85

price *= months

if contraction == "two":
    discount = price * (3.75/100)
    price -= discount

print(f"{price:.2f} lv.")