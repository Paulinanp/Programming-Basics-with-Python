width = int(input())
lenght = int(input())

cake_pieces = width * lenght
cake_taken = 0

curr_input = input()

while curr_input != 'STOP':
    pieces = int(curr_input)
    cake_taken += pieces

    if cake_taken >= cake_pieces:
        break

    curr_input = input()

pieces_left = abs(cake_pieces - cake_taken)
if cake_pieces > cake_taken:
    print(f"{pieces_left} pieces are left.")
else:
    print(f"No more cake left! You need {pieces_left} pieces more.")

