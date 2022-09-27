lenght = int(input())
weight = int(input())
height = int(input())
percent = float(input())

volume = lenght * height * weight

volumeInLiters = volume / 1000

notEmptySpace = percent / 100

emptySpace = volumeInLiters * (1 - notEmptySpace)

print(emptySpace)