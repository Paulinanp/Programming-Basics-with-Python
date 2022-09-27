import math

radius = float(input())

parameter = 2 * radius * math.pi
area = math.pi * radius * radius

print(format(area, ".2f"))
print(format(parameter, ".2f"))