size_of_egg = input()
color_of_egg = input()
count = int(input())

price = 0
cost = 0

if size_of_egg == "Large":

    if color_of_egg == "Red":
        price = 16
    elif color_of_egg == "Green":
        price = 12
    elif color_of_egg == "Yellow":
        price = 9

elif size_of_egg == "Medium":

    if color_of_egg == "Red":
        price = 13
    elif color_of_egg == "Green":
        price = 9
    elif color_of_egg == "Yellow":
        price = 7

elif size_of_egg == "Small":

    if color_of_egg == "Red":
        price = 9
    elif color_of_egg == "Green":
        price = 8
    elif color_of_egg == "Yellow":
        price = 5

final_price = price * count
cost = final_price * 0.35
final_price -= cost

print(f"{final_price:.2f} leva.")