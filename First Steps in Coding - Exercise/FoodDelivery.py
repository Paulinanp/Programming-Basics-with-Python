delivery = 2.5

countChikenMenu = int(input())
countFishMenu = int(input())
countVegMenu = int(input())

priceChikenMenu = countChikenMenu * 10.35
priceFishMenu = countFishMenu * 12.40
priceVegMenu = countVegMenu * 8.15

sum = priceVegMenu + priceFishMenu + priceChikenMenu

desert = sum * 0.2

finalSum = sum + desert + delivery

print(finalSum)