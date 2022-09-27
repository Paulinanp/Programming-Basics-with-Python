season = input()
type_of_group = input()
students_count = int(input())
nights_count = int(input())

price_nights = 0
discount = 0
sport = " "

if season == "Winter":
    if type_of_group == "boys" or type_of_group == "girls":
        price_nights = 9.6
    elif type_of_group == "mixed":
        price_nights = 10
elif season == "Spring":
    if type_of_group == "boys" or type_of_group == "girls":
        price_nights = 7.2
    elif type_of_group == "mixed":
        price_nights = 9.5
elif season == "Summer":
    if type_of_group == "boys" or type_of_group == "girls":
        price_nights = 15
    elif type_of_group == "mixed":
        price_nights = 20

final_price = price_nights * students_count * nights_count

if students_count >= 50:
    discount = final_price * 0.5
    final_price -= discount
elif 50 > students_count >= 20:
    discount = final_price * 0.15
    final_price -= discount
elif 20 > students_count >= 10:
    discount = final_price * 0.05
    final_price -= discount

if season == "Winter":
    if type_of_group == "boys":
        sport = "Judo"
    elif type_of_group == "girls":
        sport = "Gymnastics"
    elif type_of_group == "mixed":
        sport = "Ski"
elif season == "Spring":
    if type_of_group == "boys":
        sport = "Tennis"
    elif type_of_group == "girls":
        sport = "Athletics"
    elif type_of_group == "mixed":
        sport = "Cycling"
elif season == "Summer":
    if type_of_group == "boys":
        sport = "Football"
    elif type_of_group == "girls":
        sport = 'Volleyball'
    elif type_of_group == "mixed":
        sport = "Swimming"

print(f"{sport} {final_price:.2f} lv.")