num = int(input())
previousSum = 0
difference = 0

for i in range(1, num * 2):
    if i == 1:
        first_num = int(input())
        second_num = int(input())
        previousSum = first_num + second_num
    else:
        first_num2 = int(input())
        second_num2 = int(input())

        curr_sum = first_num2 + second_num2

        if abs(curr_sum - previousSum) > difference:
            difference = abs(curr_sum - previousSum)

        previousSum = curr_sum

if difference > 0:
    print(f"No, maxdiff={difference}")
else:
    print(f"Yes, value={previousSum}")




