from math import floor, ceil

days = int(input())
allFoodKg = int(input())
dogFoodKg = float(input())
catFoodKg = float(input())
turtleFoodG = float(input())

turtleFoodKg = turtleFoodG / 1000
neededFood = (dogFoodKg + catFoodKg + turtleFoodKg) * days

if allFoodKg >= neededFood:
    foodLeft = allFoodKg - neededFood
    print(f"{floor(foodLeft)} kilos of food left.")
else:
    foodNeed = neededFood - allFoodKg
    print(f"{ceil(foodNeed)} more kilos of food are needed.")