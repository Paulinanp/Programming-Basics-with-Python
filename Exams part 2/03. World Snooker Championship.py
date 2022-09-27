type_of_competition = input()
type_of_ticket = input()
tickets_cnt = int(input())
photo = input()

total_price = 0
discount = 0
photo_price = 0

if type_of_competition == "Quarter final":

    if type_of_ticket == "Standard":
        price = 55.50
    elif type_of_ticket == "Premium":
        price = 105.20
    elif type_of_ticket == "VIP":
        price = 118.90

elif type_of_competition == "Semi final":

    if type_of_ticket == "Standard":
        price = 75.88
    elif type_of_ticket == "Premium":
        price = 125.22
    elif type_of_ticket == "VIP":
        price = 300.40

elif type_of_competition == "Final":

    if type_of_ticket == "Standard":
        price = 110.10
    elif type_of_ticket == "Premium":
        price = 160.66
    elif type_of_ticket == "VIP":
        price = 400

total_price = price * tickets_cnt

if photo == "Y":
    photo_price = 40

if total_price > 4000:
    discount = total_price * 0.25
    total_price -= discount
    if photo == "Y":
        photo_price = 0
elif 4000 >= total_price > 2500:
    discount = total_price * 0.1
    total_price -= discount

total_price += tickets_cnt * photo_price

print(f"{total_price:.2f}")
