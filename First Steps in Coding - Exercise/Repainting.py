neededAmountNylon = int(input())
neededAmountPaint = int(input())
amountThinner = int(input())
hoursPerWork = int(input())

priceNylon = (neededAmountNylon + 2) * 1.50
pricePaint = (neededAmountPaint + neededAmountPaint * 0.1) * 14.5
priceThinner = amountThinner * 5
bag = 0.4

sumForMaterials = priceThinner + pricePaint + priceNylon + bag

sumForWorkers = (sumForMaterials * 0.3) * hoursPerWork

finalSum = sumForWorkers + sumForMaterials

print(finalSum)