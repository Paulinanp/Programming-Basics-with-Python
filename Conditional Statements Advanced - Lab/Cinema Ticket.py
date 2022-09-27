day = input()
price = 0

is_12lv_day = ["Monday", "Tuesday", "Friday"]
is_14lv_day = ["Wednesday", "Thursday"]
is_16lv_day = ["Saturday", "Sunday"]

if day in is_12lv_day:
    price = 12
elif day in is_14lv_day:
    price = 14
elif day in is_16lv_day:
    price = 16

print(price)