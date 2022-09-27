number = int(input())

right_sum = 0
left_sum = 0

for i in range(number * 2):
    num = int(input())

    if i < number:
        left_sum += num
    else:
        right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
