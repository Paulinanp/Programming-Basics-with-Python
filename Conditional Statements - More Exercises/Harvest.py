from math import ceil, floor

area_in_m = int(input())
grapes_for_1m = float(input())
needed_litters_wine = int(input())
count_workers = int(input())

total_grapes = area_in_m * grapes_for_1m
wine = total_grapes * 0.40
wine_total = wine / 2.5

if needed_litters_wine <= wine_total:
    wineLeft = wine_total - needed_litters_wine
    wine_per_worker = wineLeft / count_workers

    print(f"Good harvest this year! Total wine: {ceil(wine_total)} liters.")
    print(f"{ceil(wineLeft)} liters left -> {ceil(wine_per_worker)} liters per person.")
else:
    wineNeed = needed_litters_wine - wine_total
    print(f"It will be a tough winter! More {floor(wineNeed)} liters wine needed.")