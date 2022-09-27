days_staying = int(input())
type_of_room = input()
rating = input()

night = days_staying - 1
discount = 0
final_price = 0

if type_of_room == "room for one person":
    room_for_one_person = 18
    final_price = room_for_one_person * night
elif type_of_room == "apartment":
    apartment = 25
    final_price = apartment * night
    if days_staying < 10:
        discount = final_price * 0.3
        final_price -= discount
    elif 10 <= days_staying <= 15:
        discount = final_price * 0.35
        final_price -= discount
    elif days_staying > 15:
        discount = final_price * 0.5
        final_price -= discount
elif type_of_room == "president apartment":
    president_apartment = 35
    final_price = president_apartment * night
    if days_staying < 10:
        discount = final_price * 0.1
        final_price -= discount
    elif 10 <= days_staying <= 15:
        discount = final_price * 0.15
        final_price -= discount
    elif days_staying > 15:
        discount = final_price * 0.2
        final_price -= discount

if rating == "positive":
    discount = final_price * 0.25
    final_price += discount
elif rating == "negative":
    discount = final_price * 0.1
    final_price -= discount

print(f"{final_price:.2f}")
