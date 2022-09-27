flour_price = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs_count = int(input())
yeast_count = int(input())

sugar_price = flour_price - (flour_price * 0.25)
eggs_price = flour_price + (flour_price * 0.1)
yeast_price = sugar_price - (sugar_price * 0.8)

final_price = (flour_price * flour_kg) + (sugar_price * sugar_kg) + (eggs_price * eggs_count) + (yeast_price * yeast_count)

print(f"{final_price:.2f}")