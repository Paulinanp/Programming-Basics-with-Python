strawberry_price = float(input())
bananas_count = float(input())
oranges_count = float(input())
olives_count = float(input())
strawberry_count = float(input())

price_for_strawberries = strawberry_price * strawberry_count
olives_price = strawberry_price / 2

price_for_olives = olives_price * olives_count
bananas_price = olives_price - (olives_price * 0.8)
oranges_price = olives_price - (olives_price * 0.4)

price_for_bananas = bananas_price * bananas_count
price_for_oranges = oranges_price * oranges_count

final_price = price_for_oranges + price_for_bananas + price_for_olives + price_for_strawberries

print(f"{final_price:.2f}")