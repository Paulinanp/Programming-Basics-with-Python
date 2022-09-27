chrysanthemums_count = int(input())
roses_count = int(input())
tulips_count = int(input())
season = input()
is_it_holiday = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0
discount = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2
    price_roses = 4.1
    price_tulips = 2.5
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.5
    price_tulips = 4.15

total_price = price_chrysanthemums * chrysanthemums_count + price_roses * roses_count + price_tulips * tulips_count

if is_it_holiday == "Y":
    total_price += total_price * 0.15

if tulips_count > 7 and season == "Spring":
    discount = total_price * 0.05
    total_price -= discount
elif roses_count >= 10 and season == "Winter":
    discount = total_price * 0.1
    total_price -= discount
if roses_count + tulips_count + chrysanthemums_count > 20:
    discount = total_price * 0.2
    total_price -= discount

total_price += 2
print(f"{total_price:.2f}")