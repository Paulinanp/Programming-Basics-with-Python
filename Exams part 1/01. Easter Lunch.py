easter_bread_count = int(input())
eggs_count = int(input())
sweets_count = int(input())

easter_bread_price = easter_bread_count * 3.2
sweets_price = sweets_count * 5.4
eggs_price = eggs_count * 4.35

eggs_paint = 0.15 * (eggs_count * 12)

final_price = eggs_price + sweets_price + easter_bread_price + eggs_paint
print(f"{final_price:.2f}")
