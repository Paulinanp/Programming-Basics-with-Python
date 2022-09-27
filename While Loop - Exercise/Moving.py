width = int(input())
lenght = int(input())
height = int(input())
volume = width * height * lenght

total_space = 0
curr_input = input()

while curr_input != "Done":
    boxes = int(curr_input)
    total_space += boxes

    if total_space >= volume:
        break

    curr_input = input()

space = abs(total_space - volume)

if volume > total_space:
    print(f"{space} Cubic meters left.")
else:
    print(f"No more free space! You need {space} Cubic meters more.")
