priceMackerel = float(input())
priceSprat = float(input())
kgBonito = float(input())
kgScad = float(input())
kgMussels = int(input())

priceMussels = kgMussels * 7.5

priceBonito = priceMackerel + 0.6 * priceMackerel
finalPriceBonito = priceBonito * kgBonito

priceScad = priceSprat + 0.8 * priceSprat
finalPriceScad = priceScad * kgScad

sum = priceMussels + finalPriceScad + finalPriceBonito

print(format(sum, ".2f"))

