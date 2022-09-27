month = input()
nighs = int(input())

discount = 0
discount_apartment = 0
apartment_price = 0
stuio_price = 0

if month == "May" or month == "October":
    stuio_price = 50
    apartment_price = 65
    if nighs > 14:
        discount = stuio_price * 0.3
        stuio_price -= discount
        discount_apartment = apartment_price * 0.1
        apartment_price -= discount_apartment
    elif nighs > 7:
        discount = stuio_price * 0.05
        stuio_price -= discount
elif month == "June" or month == "September":
    stuio_price = 75.2
    apartment_price = 68.7
    if nighs > 14:
        discount = stuio_price * 0.2
        stuio_price -= discount
        discount_apartment = apartment_price * 0.1
        apartment_price -= discount_apartment
elif month == "July" or month == "August":
    stuio_price = 76
    apartment_price = 77
    if nighs > 14:
        discount_apartment = apartment_price * 0.1
        apartment_price -= discount_apartment

print(f"Apartment: {nighs * apartment_price:.2f} lv.")
print(f"Studio: {nighs * stuio_price:.2f} lv.")
