name_of_city = input()
type_of_package = input()
vip_discount = input()
days = int(input())

price = 0
discount = 0

cities = ["Bansko", "Borovets", "Varna", "Burgas"]
packages = ["noEquipment", "withEquipment", "noBreakfast", "withBreakfast"]

if days > 0:
    if days > 7:
        days -= 1

    if name_of_city == "Bansko" or name_of_city == "Borovets":
        if type_of_package == "withEquipment":
            price = 100
            if vip_discount == "yes":
                discount = price * 0.1
                price -= discount
        elif type_of_package == "noEquipment":
            price = 80
            if vip_discount == "yes":
                discount = price * 0.05
                price -= discount
    elif name_of_city == "Varna" or name_of_city == "Burgas":
        if type_of_package == "withBreakfast":
            price = 130
            if vip_discount == "yes":
                discount = price * 0.12
                price -= discount
        elif type_of_package == "noBreakfast":
            price = 100
            if vip_discount == "yes":
                discount = price * 0.07
                price -= discount

    if name_of_city not in cities:
        print("Invalid input!")
    if type_of_package not in packages:
        print("Invalid input!")

    if name_of_city in cities and type_of_package in packages:
        print(f"The price is {price * days:.2f}lv! Have a nice time!")

else:
    print("Days must be positive number!")