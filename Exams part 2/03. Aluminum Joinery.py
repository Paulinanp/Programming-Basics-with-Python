joinery_cnt = int(input())
joinery_type = input()
order_type = input()

price = 0
discount = 0
delivery = 60

if joinery_cnt < 10:
    print("Invalid order")
else:

    if joinery_type == "90X130":
        price = 110 * joinery_cnt
        if joinery_cnt > 60:
            discount = price * 0.08
            price -= discount
        elif joinery_cnt > 30:
            discount = price * 0.05
            price -= discount
    elif joinery_type == "100X150":
        price = 140 * joinery_cnt
        if joinery_cnt > 80:
            discount = price * 0.1
            price -= discount
        elif joinery_cnt > 40:
            discount = price * 0.06
            price -= discount
    elif joinery_type == "130X180":
        price = 190 * joinery_cnt
        if joinery_cnt > 50:
            discount = price * 0.12
            price -= discount
        elif joinery_cnt > 20:
            discount = price * 0.07
            price -= discount
    elif joinery_type == "200X300":
        price = 250 * joinery_cnt
        if joinery_cnt > 50:
            discount = price * 0.14
            price -= discount
        elif joinery_cnt > 25:
            discount = price * 0.09
            price -= discount

    if order_type == "With delivery":
        price += delivery

    if joinery_cnt > 99:
        discount = price * 0.04
        price -= discount

    print(f"{price:.2f} BGN")