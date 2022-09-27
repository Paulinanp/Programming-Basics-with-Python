budget = float(input())
season = input()

class_of_car = " "
type_of_car = " "
price_car = 0

if budget <= 100:
    class_of_car = "Economy class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.35
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.65
elif 100 < budget <= 500:
    class_of_car = "Compact class"
    if season == "Summer":
        type_of_car = "Cabrio"
        price_car = budget * 0.45
    elif season == "Winter":
        type_of_car = "Jeep"
        price_car = budget * 0.8
elif budget > 500:
    class_of_car = "Luxury class"
    type_of_car = "Jeep"
    price_car = budget * 0.9

print(class_of_car)
print(f"{type_of_car} - {price_car:.2f}")

