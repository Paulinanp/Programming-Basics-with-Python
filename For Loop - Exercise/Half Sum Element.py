import sys

num = int(input())

max_num = -sys.maxsize
num_sum = 0

for i in range(0, num):
    curr_num = int(input())

    if curr_num > max_num:
        max_num = curr_num

    num_sum += curr_num

num_sum -= max_num

if num_sum == max_num:
    print(f"Yes\nSum = {num_sum}")
else:
    diff = abs(num_sum - max_num)
    print(f"No\nDiff = {diff}")