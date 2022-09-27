from math import ceil, floor

count_magnilias = int(input())
count_hyacinths = int(input())
count_roses = int(input())
count_cactuses = int(input())
price_gift = float(input())

tax = 0

price_magnilias = count_magnilias * 3.25
price_hyacinths = count_hyacinths * 4
price_roses = count_roses * 3.5
price_cactuses = count_cactuses * 8

all_sum = price_cactuses + price_roses + price_hyacinths + price_magnilias
tax = all_sum * 0.05
all_sum -= tax

if all_sum >= price_gift:
    money_left = all_sum - price_gift
    print(f"She is left with {floor(money_left)} leva.")
else:
    money_need = price_gift - all_sum
    print(f"She will have to borrow {ceil(money_need)} leva.")