num = int(input())

sum_of_nums = 0

while True:
    current_num = int(input())
    sum_of_nums += current_num

    if sum_of_nums >= num:
        print(sum_of_nums)
        break



