text = input()

points = 0
total_sum = 0

for char in text:
    if char == "a":
        points = 1
        total_sum += points
    elif char == 'e':
        points = 2
        total_sum += points
    elif char == 'i':
        points = 3
        total_sum += points
    elif char == "o":
        points = 4
        total_sum += points
    elif char == 'u':
        points = 5
        total_sum += points

print(total_sum)
