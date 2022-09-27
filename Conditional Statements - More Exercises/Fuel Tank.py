typeFuel = input()
litters = float(input())

if typeFuel == "Diesel" or typeFuel == "Gas" or typeFuel == "Gasoline":
    if litters >= 25:
        print(f"You have enough {typeFuel.lower()}.")
    else:
        print(f"Fill your tank with {typeFuel.lower()}!")
else:
    print("Invalid fuel!")