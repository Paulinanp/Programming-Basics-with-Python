countPens = int(input())
countMarkers = int(input())
littersPreparation = int(input())
discount = int(input())

priceForPens = countPens * 5.8
priceForMarkers = countMarkers * 7.2
priceForPreparation = littersPreparation * 1.2

sum = priceForPreparation + priceForMarkers + priceForPens
finalSum = sum - (sum * (discount / 100))

print(finalSum)