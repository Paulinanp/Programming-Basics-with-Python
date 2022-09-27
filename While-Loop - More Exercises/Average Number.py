num = int(input())

sum_of_nums = 0
cnt = 1

while cnt <= num:
    curr_inp = int(input())
    sum_of_nums += curr_inp
    cnt += 1

print(f"{sum_of_nums / num:.2f}")
