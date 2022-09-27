product = input()
day = input()
quantity = float(input())
price = 0
is_valid = True

working_days = ['Monday', "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]

if day in working_days:
    if product == "banana":
        price = 2.5
    elif product == "apple":
        price = 1.2
    elif product == "orange":
        price = 0.85
    elif product == "grapefruit":
        price = 1.45
    elif product == "kiwi":
        price = 2.7
    elif product == "pineapple":
        price = 5.5
    elif product == "grapes":
        price = 3.85
    else:
        is_valid = False
elif day in weekend:
    if product == "banana":
        price = 2.7
    elif product == "apple":
        price = 1.25
    elif product == "orange":
        price = 0.9
    elif product == "grapefruit":
        price = 1.6
    elif product == "kiwi":
        price = 3
    elif product == "pineapple":
        price = 5.6
    elif product == "grapes":
        price = 4.2
    else:
        is_valid = False
else:
    is_valid = False

if is_valid:
    print(f"{price * quantity:.2f}")
else:
    print("error")
