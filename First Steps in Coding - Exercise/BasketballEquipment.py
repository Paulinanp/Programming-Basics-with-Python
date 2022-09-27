taxPerYear = int(input())

basketballShoes = taxPerYear - taxPerYear * 0.4
basketballOutfit = basketballShoes - basketballShoes * 0.2
basketballBall = basketballOutfit / 4
basketballAccessories = basketballBall / 5

sum = basketballAccessories + basketballShoes + basketballBall + basketballOutfit + taxPerYear

print(sum)