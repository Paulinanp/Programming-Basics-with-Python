from math import ceil

people_count = int(input())
entry_tax = float(input())
price_sunbed = float(input())
umbrella_price = float(input())

sunbed_count = ceil(people_count * 0.75)
umbrella_count = ceil(people_count / 2)

total_entry_price = people_count * entry_tax
total_umbrella_price = umbrella_price * umbrella_count
total_sunbed_price = sunbed_count * price_sunbed

final_sum = total_sunbed_price + total_entry_price + total_umbrella_price

print(f"{final_sum:.2f} lv.")
