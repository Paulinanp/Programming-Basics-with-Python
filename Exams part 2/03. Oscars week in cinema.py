name_of_film = input()
type_of_hall = input()
tickets_count = int(input())

price = 0

if name_of_film == "A Star Is Born":

    if type_of_hall == "normal":
        price = 7.5
    elif type_of_hall == "luxury":
        price = 10.5
    elif type_of_hall == "ultra luxury":
        price = 13.5

elif name_of_film == "Bohemian Rhapsody":

    if type_of_hall == "normal":
        price = 7.35
    elif type_of_hall == "luxury":
        price = 9.45
    elif type_of_hall == "ultra luxury":
        price = 12.75

elif name_of_film == "Green Book":

    if type_of_hall == "normal":
        price = 8.15
    elif type_of_hall == "luxury":
        price = 10.25
    elif type_of_hall == "ultra luxury":
        price = 13.25

elif name_of_film == "The Favourite":

    if type_of_hall == "normal":
        price = 8.75
    elif type_of_hall == "luxury":
        price = 11.55
    elif type_of_hall == "ultra luxury":
        price = 13.95

price *= tickets_count

print(f"{name_of_film} -> {price:.2f} lv.")
