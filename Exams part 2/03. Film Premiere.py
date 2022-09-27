name_of_film = input()
package_for_film = input()
tickets_count = int(input())

price = 0
discount = 0

if name_of_film == "John Wick":

    if package_for_film == "Drink":
        price = 12
    elif package_for_film == "Popcorn":
        price = 15
    elif package_for_film == "Menu":
        price = 19

elif name_of_film == "Star Wars":

    if package_for_film == "Drink":
        price = 18
    elif package_for_film == "Popcorn":
        price = 25
    elif package_for_film == "Menu":
        price = 30

elif name_of_film == "Jumanji":

    if package_for_film == "Drink":
        price = 9
    elif package_for_film == "Popcorn":
        price = 11
    elif package_for_film == "Menu":
        price = 14

price *= tickets_count

if name_of_film == "Star Wars" and tickets_count >= 4:
    discount = price * 0.3
    price -= discount

if name_of_film == "Jumanji" and tickets_count == 2:
    discount = price * 0.15
    price -= discount

print(f"Your bill is {price:.2f} leva.")