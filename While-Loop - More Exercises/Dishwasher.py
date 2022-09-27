bottles_cnt = int(input())
counter = 1
curr_input = input()
dishes_cnt = 0
pots_cnt = 0

liquid = bottles_cnt * 750

while curr_input != "End":
    subject = int(curr_input)

    if counter % 3 == 0:
        liquid -= subject * 15
        pots_cnt += subject
    else:
        liquid -= subject * 5
        dishes_cnt += subject

    if liquid < 0:
        print(f"Not enough detergent, {abs(liquid)} ml. more necessary!")
        break

    counter += 1
    curr_input = input()

if liquid >= 0:
    print("Detergent was enough!")
    print(f"{dishes_cnt} dishes and {pots_cnt} pots were washed.")
    print(f"Leftover detergent {liquid} ml.")
