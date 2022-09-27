metersGreening = float(input())

priceForGreening = metersGreening * 7.61
discount = priceForGreening * 0.18

finalPrice = priceForGreening - discount

print(f"The final price is: {finalPrice}")
print(f"The discount is: {discount}")