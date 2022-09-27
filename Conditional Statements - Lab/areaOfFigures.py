from math import pi

figure = input()
area = 0

if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    sideA = float(input())
    sideB = float(input())
    area = sideA * sideB
elif figure == "circle":
    radius = float(input())
    area = pi * radius * radius
elif figure == "triangle":
    side = float(input())
    height = float(input())
    area = (side * height) / 2

print(f"{area:.3f}")
