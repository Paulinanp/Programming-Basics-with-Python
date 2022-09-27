priceVegetabbles = float(input())
priceFruits = float(input())
kgVegetabbles = int(input())
kgFruits = int(input())

finalPriceFruits = priceFruits * kgFruits
finalPriceVegetables = priceVegetabbles * kgVegetabbles

priceInEuro = (finalPriceVegetables + finalPriceFruits) / 1.94
print(format(priceInEuro, ".2f"))