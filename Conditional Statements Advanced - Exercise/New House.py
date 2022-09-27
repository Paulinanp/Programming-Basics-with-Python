type_of_flower = input()
count_flowers = int(input())
budget = int(input())
price = 0
discount = 0

if type_of_flower == "Roses":
    roses_price = 5
    price = roses_price * count_flowers
    if count_flowers > 80:
        discount = price * 0.1
        price -= discount
if type_of_flower == "Dahlias":
    dahlias_price = 3.8
    price = dahlias_price * count_flowers
    if count_flowers > 90:
        discount = price * 0.15
        price -= discount
if type_of_flower == "Tulips":
    tulips_price = 2.8
    price = tulips_price * count_flowers
    if count_flowers > 80:
        discount = price * 0.15
        price -= discount
if type_of_flower == "Narcissus":
    narcissus_price = 3
    price = narcissus_price * count_flowers
    if count_flowers < 120:
        discount = price * 0.15
        price += discount
if type_of_flower == "Gladiolus":
    gladiolus_price = 2.5
    price = gladiolus_price * count_flowers
    if count_flowers < 80:
        discount = price * 0.2
        price += discount

if budget >= price:
    money_left = budget - price
    print(f"Hey, you have a great garden with {count_flowers}"
          f" {type_of_flower} and {money_left:.2f} leva left.")
else:
    money_need = price - budget
    print(f"Not enough money, you need {money_need:.2f} leva more.")