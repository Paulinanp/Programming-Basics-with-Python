price_trip = float(input())
count_puzzles = int(input())
count_dolls = int(input())
count_bears = int(input())
count_minions = int(input())
count_trucks = int(input())

discount = 0

price_puzzles = 2.6 * count_puzzles
price_dolls = 3 * count_dolls
price_bears = 4.1 * count_bears
price_minions = 8.20 * count_minions
price_trucks = 2 * count_trucks

price_for_allToys = price_trucks + price_bears + price_dolls + price_puzzles + price_minions
totalToys = count_trucks + count_bears + count_dolls + count_minions + count_puzzles

if totalToys >= 50:
    discount = price_for_allToys * 0.25

rent = (price_for_allToys - discount) * 0.1

finalPrice = price_for_allToys - discount - rent

if finalPrice >= price_trip:
    moneyLeft = finalPrice - price_trip
    print(f"Yes! {moneyLeft:.2f} lv left.")
else:
    moneyNeeded = price_trip - finalPrice
    print(f"Not enough money! {moneyNeeded:.2f} lv needed.")